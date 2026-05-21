from datetime import datetime, timedelta
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, SignupSerializer, LoginSerializer


def generate_tokens(user):
    """Generate JWT access and refresh tokens."""
    access_payload = {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow(),
    }
    
    refresh_payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=7),
        'iat': datetime.utcnow(),
    }
    
    access_token = jwt.encode(access_payload, settings.JWT_SECRET, algorithm='HS256')
    refresh_token = jwt.encode(refresh_payload, settings.JWT_SECRET, algorithm='HS256')
    
    return access_token, refresh_token


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            access_token, refresh_token = generate_tokens(user)
            return Response({
                'success': True,
                'user': UserSerializer(user).data,
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            if not user.check_password(serializer.validated_data['password']):
                return Response({'success': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'success': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        access_token, refresh_token = generate_tokens(user)
        return Response({
            'success': True,
            'user': UserSerializer(user).data,
            'access_token': access_token,
            'refresh_token': refresh_token,
        })


class LogoutView(APIView):
    def post(self, request):
        return Response({'success': True, 'message': 'Logged out successfully'})


class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'success': False, 'message': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            payload = jwt.decode(refresh_token, settings.JWT_SECRET, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            access_token, new_refresh_token = generate_tokens(user)
            return Response({
                'success': True,
                'access_token': access_token,
                'refresh_token': new_refresh_token,
            })
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
            return Response({'success': False, 'message': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({
            'success': True,
            'user': UserSerializer(request.user).data,
        })
    
    def put(self, request):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'user': serializer.data})
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

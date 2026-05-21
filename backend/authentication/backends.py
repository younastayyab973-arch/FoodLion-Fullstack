import jwt
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class JWTAuthentication(TokenAuthentication):
    """JWT authentication backend."""
    
    def authenticate(self, request):
        auth = self.get_authorization_header(request).split()
        
        if not auth or auth[0].lower() != b'bearer':
            return None
        
        if len(auth) == 1:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth) > 2:
            raise AuthenticationFailed('Invalid token header. Token string should not contain spaces.')
        
        try:
            token = auth[1].decode('utf-8')
        except UnicodeDecodeError:
            raise AuthenticationFailed('Invalid token encoding.')
        
        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, settings.JWT_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        
        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
        
        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        
        return (user, key)

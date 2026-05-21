from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AdminAPIView(APIView):
    """Base class ensuring only admins can access."""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().dispatch(request, *args, **kwargs)

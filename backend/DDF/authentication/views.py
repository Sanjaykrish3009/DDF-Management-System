from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.utils.decorators import method_decorator
from user.models import UserProfile
    

@method_decorator(ensure_csrf_cookie,name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,format=None):
        return Response({'success':'CSRF cookie set'})
    

class CheckAuthenticatedView(APIView):
    
    def get(self,request,format=None):
        user = self.request.user
        
        try:
            isAuthenticated = user.is_authenticated
            user_profile = UserProfile.objects.get(user=user)
            type = user_profile.get_user_type()
            if isAuthenticated:
                return Response({'isAuthenticated':'success', 'user_type': type})
            else:
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error':'Something went wrong when checking authentication status'})


@method_decorator(csrf_protect,name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self,request,format=None):
        data = self.request.data
        email = data['email']
        password = data['password']

        try:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request,user)
                user_profile = UserProfile.objects.get(user=user)
                type = user_profile.get_user_type()
                return Response({'success': 'User authenticated','user_type':type})            
            else:
                return Response({'error': 'Invalid Credentials'})
        except:
            return Response({'error':'Something went wrong while logging in'})
        

class LogoutView(APIView):
    def post(self,request,format=None):
        try:
            logout(request)
            return Response({'success': 'Logout Successful'})
        except:
            return Response({'error':'Something went wrong when logging out'})

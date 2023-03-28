from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.utils.decorators import method_decorator
from .models import CustomUser, FacultyUser, CommitteeUser, HodUser, FundRequest


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

            if isAuthenticated:
                return Response({'isAuthenticated':'success'})
            else:
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error':'Something went wrong when checking authentication status'})
    
@method_decorator(csrf_protect,name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):

        data = self.request.data
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']        
        password = data['password']
        re_password = data['re_password']

        try:
            if password == re_password:
                if FacultyUser.objects.filter(email=email).exists():
                    return Response({ 'error': 'email already exists' })
                else:
                    if len(password)<6:
                        return Response({'error':'Password must be atleast 6 characters'})
                    else:
                        FacultyUser.objects.create_user(email, first_name, last_name, password)
                        return Response({'success':'User created successfully'})
            else:
                return Response({'error':'Passwords do not match'})
        except:
            return Response({'error':'Something went wrong while registering an account'})

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
                type=self.user_type(user)
                return Response({'success': 'User authenticated','user_type':type})            
            else:
                return Response({'error': 'Invalid Credentials'})
        except:
            return Response({'error':'Something went wrong while logging in'})
        
    def user_type(self, user):
        if hasattr(user, 'faculty_id'):
            return 'faculty'
        elif hasattr(user, 'committee_id'):
            return 'committee'
        elif hasattr(user, 'hod_id'):
            return 'hod'
        else:
            return 'unknown'

class LogoutView(APIView):
    def post(self,request,format=None):
        try:
            logout(request)
            return Response({'success': 'Logout Successful'})
        except:
            return Response({'error':'Something went wrong when logging out'})

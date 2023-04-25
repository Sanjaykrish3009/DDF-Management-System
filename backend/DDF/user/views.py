from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from faculty.models import FacultyUser
from committee.models import CommitteeUser
from hod.models import HodUser
from .models import UserProfile
from django.contrib.auth import logout


@method_decorator(csrf_protect,name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):

        data = self.request.data

        if 'first_name' not in data:
            return Response({'error': 'First Name field must be set'})
        
        if 'last_name' not in data:
            return Response({'error': 'Last Name field must be set'})
        
        if 'email' not in data:
            return Response({'error': 'Email field must be set'})
        
        if 'password' not in data:
            return Response({'error': 'Password field must be set'})
        
        if 're_password' not in data:
            return Response({'error': 'Re Password field must be set'})
        
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
                        faculty_user = FacultyUser.objects.create_user(email, password)
                        user_profile = UserProfile(user=faculty_user, first_name=first_name, last_name=last_name, user_type='faculty')
                        user_profile.save()                        
                        return Response({'success':'User created successfully'})
            else:
                return Response({'error':'Passwords do not match'})
        except:
            return Response({'error':'Something went wrong while registering an account'})
    

class ProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
            profile = user_profile.get_user_profile()
            return Response({'profile':profile})
        except:
            return Response({'error':'Something went wrong while retrieving Profile'})
           
class ChangePasswordView(APIView):
    def post(self, request, format=None):
        data = self.request.data

        if 'old_password' not in data:
            return Response({'error': 'Old Password field must be set'})
        
        if 'new_password' not in data:
            return Response({'error': 'New Password field must be set'})
        
        if 're_new_password' not in data:
            return Response({'error': 'Re New Password field must be set'})
        
        old_password = data['old_password']
        new_password = data['new_password']
        re_new_password = data['re_new_password']
        user = self.request.user

        try:
            if user.check_password(old_password):
                if new_password == re_new_password:
                    if len(new_password) < 6:
                        return Response({'error': 'Password must be at least 6 characters' })
                    else:
                        user.set_password(new_password)
                        user.save()
                        logout(request)
                        return Response({'success': 'Password Changed successfully'})
                else:
                    return Response({ 'error': 'Passwords do not match' })
            else:
                return Response({ 'error': 'Incorrect Old Password' })
        except:
            return Response({'error': 'Something went wrong when changing password'})
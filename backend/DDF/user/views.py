from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from faculty.models import FacultyUser
from .models import UserProfile
from authentication.models import CustomUser

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
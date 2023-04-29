from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from authentication.models import CustomUser
from faculty.models import FacultyUser
from committee.models import CommitteeUser
from hod.models import HodUser
from .models import UserProfile
from django.contrib.auth import logout
from django.core.mail import send_mail
from datetime import timedelta
import json, random, string, datetime
from django.utils import timezone

@method_decorator(csrf_protect,name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):

        data = self.request.data

        if 'first_name' not in data:
            return Response({'error':'First Name field must be set'})
        
        if 'last_name' not in data:
            return Response({'error':'Last Name field must be set'})
        
        if 'email' not in data:
            return Response({'error':'Email field must be set'})

        if 'password' not in data:
            return Response({'error':'Password field must be set'})
        
        if 're_password' not in data:
            return Response({'error':'Re Password field must be set'})
        
        email = data['email']        
        password = data['password']
        re_password = data['re_password']

        # if email.endswith("@cse.iith.ac.in")==False:
        #     return Response({'error':'Email should end with @cse.iith.ac.in'})
        
        try:
            if password == re_password:
                if CustomUser.objects.filter(email=email).exists():
                    return Response({ 'error': 'email already exists' })
                else:
                    if len(password)<6:
                        return Response({'error':'Password must be atleast 6 characters'})
                    else:
                        otp = ''.join(random.choices(string.digits, k=6))
                        otp_created_at = timezone.now()
                        otp_data = {'otp': otp, 'otp_created_at': otp_created_at}
                        otp_data_json = json.dumps(otp_data, default=str)
                        request.session['reset_otp_data'] = otp_data_json
                        request.session['reset_email'] = email
                        subject = 'DDF Account Email Verification'
                        message = f'Your OTP for verification to create a DDF Management System Account with this email is: {otp}'
                        from_email = 'ddf.cse.iith@gmail.com' 
                        recipient_list = [email]
                        send_mail(subject, message, from_email, recipient_list)   
                        return Response({'success':'OTP sent for email verification', 'otp': otp, 'otp_created_at': otp_created_at})
            else:
                return Response({'error':'Passwords do not match'})
        except:
            return Response({'error':'Something went wrong while registering an account'})
    

@method_decorator(csrf_protect, name='dispatch')
class CheckEmailView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        if 'entered_otp' not in data:
            return Response({'error': 'OTP field must be set'})
        
        entered_otp = data['entered_otp']
        otp_data_json = request.session.get('reset_otp_data')
        otp_data = json.loads(otp_data_json)
        sent_otp = otp_data['otp']
        otp_created_at_str = otp_data['otp_created_at']
        otp_created_at = datetime.datetime.strptime(otp_created_at_str, '%Y-%m-%d %H:%M:%S.%f%z')
        otp_age = timezone.now() - otp_created_at
        if not sent_otp or not entered_otp or entered_otp != sent_otp:
            return Response({'error': 'Invalid OTP'})
        elif otp_age > timedelta(minutes=5):
            return Response({'error': 'Invalid OTP'})
        else:
            del request.session['reset_otp_data']
            self.request.session['otp_verified'] = True

            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']        
            password = data['password']

            if email=='cs19btech11022@iith.ac.in':
                hod_user = HodUser.objects.create_user(email, password)
                user_profile = UserProfile(user=hod_user, first_name=first_name, last_name=last_name, user_type='hod')
                user_profile.save() 
            elif email == 'cs19btech11006@iith.ac.in':
                committee_user = CommitteeUser.objects.create_user(email, password)
                user_profile = UserProfile(user=committee_user, first_name=first_name, last_name=last_name, user_type='committee')
                user_profile.save() 
            else:
                faculty_user = FacultyUser.objects.create_user(email, password)
                user_profile = UserProfile(user=faculty_user, first_name=first_name, last_name=last_name, user_type='faculty')
                user_profile.save()        

            return Response({'success':'User created successfully'}) 


class ProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
            profile = user_profile.get_user_profile()
            return Response({'success':'Profile retrieved Succesfully','profile':profile})
        except:
            return Response({'error':'Something went wrong while retrieving Profile'})
           
class ChangePasswordView(APIView):
    def post(self, request, format=None):
        data = self.request.data

        if 'old_password' not in data:
            return Response({'error':'Old Password field must be set'})
        
        if 'new_password' not in data:
            return Response({'error':'New Password field must be set'})
        
        if 're_new_password' not in data:
            return Response({'error':'Re Enter New Password field must be set'})
        
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
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from django.utils.decorators import method_decorator
from user.models import UserProfile
from .models import CustomUser
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import json, random, string, datetime
    

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
                return Response({'isAuthenticated':'success', 'type': type})
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


@method_decorator(csrf_protect, name='dispatch')
class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny, )

    def generate_otp(self):
        otp = ''.join(random.choices(string.digits, k=6))
        return f'{otp}'

    def post(self, request, format=None):
        data = self.request.data
        email = data['email']
        try:
            user = CustomUser.objects.get(email=email)
        except:
            return Response({'error': 'User doesnot exist with given email'})
        else:
            otp = self.generate_otp()
            otp_created_at = timezone.now()
            otp_data = {'otp': otp, 'otp_created_at': otp_created_at}
            otp_data_json = json.dumps(otp_data, default=str)
            request.session['reset_otp_data'] = otp_data_json
            request.session['reset_email'] = email
            subject = 'DDF Account Password Reset Request'
            message = f'Your OTP for resetting the password for your DDF Management System Account registered with this email is: {otp}'
            from_email = 'ddf.cse.iith@gmail.com' 
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            
            return Response({'success': 'OTP sent to Registered Email'})


@method_decorator(csrf_protect, name='dispatch')
class CheckOtpView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
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
            return Response({'success': 'OTP verifed'})


@method_decorator(csrf_protect, name='dispatch')
class ResetPasswordView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        email = request.session['reset_email']
        user = CustomUser.objects.get(email=email)
        new_password = data['new_password']
        re_new_password = data['re_new_password']

        if new_password == re_new_password:
            if len(new_password) < 6:
                return Response({'error': 'Password must be at least 6 characters' })
            else:
                user.set_password(new_password)
                user.save()
                del request.session['reset_email']
                subject = 'DDF Account Password Reset Successful'
                message = f'Password for your DDF Account has been reset.'
                from_email = 'ddf.cse.iith@gmail.com' 
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list)
                return Response({'success': 'Password Reset successful'})
        else:
            return Response({ 'error': 'Passwords do not match' })

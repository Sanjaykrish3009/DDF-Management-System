from django.urls import path
from .views import GetCSRFToken,CheckAuthenticatedView,LoginView,LogoutView,ForgotPasswordView,CheckOtpView,ResetPasswordView

app_name = 'authentication'

urlpatterns = [
    path('csrf_cookie',GetCSRFToken.as_view(), name='getcsrftoken'),
    path('authenticated',CheckAuthenticatedView.as_view(), name='checkauthentication'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('forgotpassword', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('checkotp', CheckOtpView.as_view(), name='checkotp'),
    path('resetpassword', ResetPasswordView.as_view(), name='resetpassword'),
]


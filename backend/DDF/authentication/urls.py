from django.urls import path
from .views import GetCSRFToken,CheckAuthenticatedView,LoginView,LogoutView,ForgotPasswordView,CheckOtpView,ResetPasswordView

urlpatterns = [
    path('csrf_cookie',GetCSRFToken.as_view()),
    path('authenticated',CheckAuthenticatedView.as_view()),
    path('login',LoginView.as_view()),
    path('logout',LogoutView.as_view()),
    path('forgotpassword', ForgotPasswordView.as_view()),
    path('checkotp', CheckOtpView.as_view()),
    path('resetpassword', ResetPasswordView.as_view()),
]


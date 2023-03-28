from django.urls import path
from .views import GetCSRFToken,CheckAuthenticatedView,LoginView,SignupView,LogoutView

urlpatterns = [
    path('csrf_cookie',GetCSRFToken.as_view()),
    path('authenticated',CheckAuthenticatedView.as_view()),
    path('register',SignupView.as_view()),
    path('login',LoginView.as_view()),
    path('logout',LogoutView.as_view()),
]


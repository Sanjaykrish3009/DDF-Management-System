from django.urls import path
from .views import SignupView, ProfileView, ChangePasswordView

app_name = 'user'

urlpatterns = [
    path('register', SignupView.as_view(),name='signup'),
    path('profile', ProfileView.as_view(),name='viewprofile'),
    path('changepassword', ChangePasswordView.as_view(),name='changepassword'),
]


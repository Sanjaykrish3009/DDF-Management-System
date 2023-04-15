from django.urls import path
from .views import PendingRequests,PreviousRequests,PublicRequests

urlpatterns = [
    path('pendingrequests', PendingRequests.as_view()),
    path('publicrequests', PublicRequests.as_view()),
    path('previousrequests', PreviousRequests.as_view()),
]


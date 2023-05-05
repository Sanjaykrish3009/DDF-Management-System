from django.urls import path
from .views import PendingRequests,PreviousRequests,PublicRequests

app_name ='faculty'
urlpatterns = [
    path('pendingrequests', PendingRequests.as_view(),name='pendingrequests'),
    path('publicrequests', PublicRequests.as_view(),name='publicrequests'),
    path('previousrequests', PreviousRequests.as_view(),name='previousrequests'),
]


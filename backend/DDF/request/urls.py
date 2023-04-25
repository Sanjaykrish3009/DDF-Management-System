from django.urls import path
from .views import CreatePrivateFundRequest, CreatePublicFundRequest, CreateBudgetRequest, RequestDetails, FileDetails

app_name = 'request'

urlpatterns = [
    path('createprivaterequest', CreatePrivateFundRequest.as_view(), name ='createprivaterequest'),
    path('createpublicrequest', CreatePublicFundRequest.as_view(), name ='createpublicrequest'),
    path('createbudgetrequest', CreateBudgetRequest.as_view(), name ='createbudgetrequest'),
    path('requestdetails', RequestDetails.as_view(), name ='requestdetails'),
    path('filedetails', FileDetails.as_view(), name ='filedetails')
]


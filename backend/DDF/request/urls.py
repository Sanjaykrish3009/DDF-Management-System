from django.urls import path
from .views import CreatePrivateFundRequest, CreatePublicFundRequest, CreateBudgetRequest, RequestDetails, FileDetails

urlpatterns = [
    path('createprivaterequest', CreatePrivateFundRequest.as_view()),
    path('createpublicrequest', CreatePublicFundRequest.as_view()),
    path('createbudgetrequest', CreateBudgetRequest.as_view()),
    path('requestdetails', RequestDetails.as_view()),
    path('filedetails', FileDetails.as_view())
]


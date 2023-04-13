from django.urls import path
from .views import CreatePrivateFundRequest, CreatePublicFundRequest, CreateBudgetRequest

urlpatterns = [
    path('createprivaterequest', CreatePrivateFundRequest.as_view()),
    path('createpublicrequest', CreatePublicFundRequest.as_view()),
    path('createbudgetrequest', CreateBudgetRequest.as_view()),
]


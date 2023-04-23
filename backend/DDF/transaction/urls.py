from django.urls import path
from .views import TransactionDetails

urlpatterns = [
    path('transactiondetails', TransactionDetails.as_view()),
]


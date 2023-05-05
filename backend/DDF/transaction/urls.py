from django.urls import path
from .views import TransactionDetails

app_name = "transaction"

urlpatterns = [
    path('transactiondetails', TransactionDetails.as_view(), name = "transactiondetails"),
]


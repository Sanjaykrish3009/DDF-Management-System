from django.urls import path
from .views import CreateTransaction, TransactionDetails

urlpatterns = [
    path('createtransaction', CreateTransaction.as_view()),
    path('transactiondetails', TransactionDetails.as_view()),
]


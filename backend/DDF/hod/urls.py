from django.urls import path
from .views import PendingRequests, PreviousRequests, Approval, Disapproval, AllTransactions, Balance, CreditRequests, DebitRequests, CreditTransactions, DebitTransactions

urlpatterns = [
    path('pendingrequests', PendingRequests.as_view()),
    path('previousrequests', PreviousRequests.as_view()),
    path('approve', Approval.as_view()),
    path('disapprove', Disapproval.as_view()),
    path('alltransactions', AllTransactions.as_view()),
    path('viewbalance', Balance.as_view()),
    path('creditrequests', CreditRequests.as_view()),
    path('debitrequests', DebitRequests.as_view()),
    path('credittransactions', CreditTransactions.as_view()),
    path('debittransactions', DebitTransactions.as_view())
]


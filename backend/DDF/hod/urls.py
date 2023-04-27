from django.urls import path
from .views import PendingRequests, PreviousRequests, Approval, Disapproval, AllTransactions, Balance, CreditRequests, DebitRequests, CreditTransactions, DebitTransactions, SendExcelSheet

app_name = 'hod'

urlpatterns = [
    path('pendingrequests', PendingRequests.as_view(), name = 'pendingrequests'),
    path('previousrequests', PreviousRequests.as_view(), name = 'previousrequests'),
    path('approve', Approval.as_view(), name = 'approve'),
    path('disapprove', Disapproval.as_view(), name = 'disapprove'),
    path('alltransactions', AllTransactions.as_view(), name = 'alltransactions'),
    path('viewbalance', Balance.as_view(), name = 'viewbalance'),
    path('creditrequests', CreditRequests.as_view(), name = 'creditrequests'),
    path('debitrequests', DebitRequests.as_view(), name = 'debitrequests'),
    path('credittransactions', CreditTransactions.as_view(), name = 'credittransactions'),
    path('debittransactions', DebitTransactions.as_view(), name = 'debittransactions'),
    path('sendexcelsheet', SendExcelSheet.as_view(), name='sendexcelsheet')
]


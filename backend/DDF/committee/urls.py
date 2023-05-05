from django.urls import path
from .views import PendingRequests,PreviousRequests, Approval, Disapproval, AllTransactions, Balance, CreditTransactions, DebitTransactions

app_name = 'committee'

urlpatterns = [
    path('pendingrequests', PendingRequests.as_view(),name = 'pendingrequests'),
    path('previousrequests', PreviousRequests.as_view(),name = 'previousrequests'),
    path('approve', Approval.as_view(),name = 'approve'),
    path('disapprove', Disapproval.as_view(),name = 'disapprove'),
    path('alltransactions', AllTransactions.as_view(),name = 'alltransactions'),
    path('viewbalance', Balance.as_view(),name = 'viewbalance'),
    path('credittransactions', CreditTransactions.as_view(),name = 'credittransactions'),
    path('debittransactions', DebitTransactions.as_view(),name = 'debittransactions'),
]


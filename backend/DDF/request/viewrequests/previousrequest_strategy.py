from .viewrequests_strategy import ViewRequestsStrategy
from request.models import FundRequest
from django.db.models import Q 

class PreviousRequestStrategy(ViewRequestsStrategy):

    def view_requests(self,user):
        requests = FundRequest.objects.filter((Q(hod_approval_status = 'Approved') | Q(committee_approval_status = 'Disapproved') | 
                                                        Q(hod_approval_status = 'Disapproved')), user=user)
        return requests
    


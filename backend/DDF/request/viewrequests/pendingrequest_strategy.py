from .viewrequests_strategy import ViewRequestsStrategy
from request.models import FundRequest
from django.db.models import Q 

class PendingRequestStrategy(ViewRequestsStrategy):

    def view_requests(self,user):
        requests = FundRequest.objects.filter((Q(committee_approval_status = 'Pending') | 
                                            Q(committee_approval_status = 'Approved', hod_approval_status = 'Pending')), user=user)
        
        return requests
    
    def search_view_requests(self,user,title):
        requests = FundRequest.objects.filter((Q(committee_approval_status = 'Pending') | 
                                            Q(committee_approval_status = 'Approved', hod_approval_status = 'Pending')), user=user,request_title__icontains=title)
        
        return requests
    


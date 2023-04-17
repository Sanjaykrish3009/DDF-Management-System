from .viewrequests_strategy import ViewRequestsStrategy
from request.models import FundRequest
from django.db.models import Q 


class ViewRequests(ViewRequestsStrategy):

    def view_pending_requests(self):
        pending_requests = FundRequest.objects.filter((Q(committee_approval_status = 'Pending') | 
                                            Q(committee_approval_status = 'Approved', hod_approval_status = 'Pending')), user=self)
        return self.fetch_requests_data(pending_requests)
    
    def view_previous_requests(self):
        previous_requests = FundRequest.objects.filter((Q(hod_approval_status = 'Approved') | Q(committee_approval_status = 'Disapproved') | 
                                                        Q(hod_approval_status = 'Disapproved')), user=self)
        return self.fetch_requests_data(previous_requests)
    
    def view_public_requests(self):
        public_requests = FundRequest.objects.filter(request_type='PublicRequest')
        return self.fetch_requests_data(public_requests)

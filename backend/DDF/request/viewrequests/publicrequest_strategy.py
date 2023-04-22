from .viewrequests_strategy import ViewRequestsStrategy
from request.models import FundRequest
from django.db.models import Q 

class PublicRequestStrategy(ViewRequestsStrategy):

    def view_requests(self,user):
        requests = FundRequest.objects.filter(request_type='PublicRequest')
        return requests
    


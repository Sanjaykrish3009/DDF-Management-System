from .viewrequests_strategy import ViewRequestsStrategy
from request.models import FundRequest
from django.db.models import Q 

class PublicRequestStrategy(ViewRequestsStrategy):

    def view_requests(self,user):
        requests = FundRequest.objects.filter(request_type='PublicRequest')
        return requests
    
    def search_view_requests(self,user,title):
        requests = FundRequest.objects.filter(request_type='PublicRequest',request_title__icontains=title)
        return requests
    


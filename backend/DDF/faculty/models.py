from django.db import models
from authentication.models import CustomUser
from request.viewrequests.pendingrequest_strategy import PendingRequestStrategy
from request.viewrequests.previousrequest_strategy import PreviousRequestStrategy
from request.viewrequests.publicrequest_strategy import PublicRequestStrategy
from request.viewrequests.context import ContextRequest

class FacultyUser(CustomUser):
    faculty_id = models.CharField(max_length=30)

    def view_pending_requests(self):
        
        context = ContextRequest(PendingRequestStrategy())
        pending_requests= context.view_requests(self)

        return self.fetch_requests_data(pending_requests)
    
    def search_view_pending_requests(self,title):
 
        context = ContextRequest(PendingRequestStrategy())
        pending_requests= context.view_requests(self)
        pending_requests = pending_requests.filter(request_title__icontains=title)

        return self.fetch_requests_data(pending_requests)
    
    def view_previous_requests(self):

        context = ContextRequest(PreviousRequestStrategy())
        previous_requests= context.view_requests(self)

        return self.fetch_requests_data(previous_requests)

    def search_view_previous_requests(self,title):

        context = ContextRequest(PreviousRequestStrategy())
        previous_requests= context.view_requests(self)
        previous_requests = previous_requests.filter(request_title__icontains=title)

        return self.fetch_requests_data(previous_requests)
    
    def view_public_requests(self):

        context = ContextRequest(PublicRequestStrategy())
        public_requests= context.view_requests(self)
       
        return self.fetch_requests_data(public_requests)
    
    def search_view_public_requests(self,title):

        context = ContextRequest(PublicRequestStrategy())
        public_requests= context.view_requests(self)
        public_requests= public_requests.filter(request_title__icontains=title)
       
        return self.fetch_requests_data(public_requests)


    def fetch_requests_data(self,requests):
        data_list = []
        
        for request_obj in requests:
            request_dict = request_obj.get_request_data()
            data_list.append(request_dict)

        sorted_data_list = sorted(data_list, key=lambda x:x['request_date'], reverse=True)
        return sorted_data_list
    

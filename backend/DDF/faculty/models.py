from django.db import models
from authentication.models import CustomUser
from request.viewrequests.pendingrequest_strategy import PendingRequestStrategy
from request.viewrequests.previousrequest_strategy import PreviousRequestStrategy
from request.viewrequests.publicrequest_strategy import PublicRequestStrategy

class FacultyUser(CustomUser):
    faculty_id = models.CharField(max_length=30)

    def view_pending_requests(self):
        PendingRequests = PendingRequestStrategy()
        pending_requests = PendingRequests.view_requests(self)

        return self.fetch_requests_data(pending_requests)
    
    def view_previous_requests(self):
        PreviousRequests = PreviousRequestStrategy()
        previous_requests = PreviousRequests.view_requests(self)

        return self.fetch_requests_data(previous_requests)
    
    def view_public_requests(self):

        PublicRequests = PublicRequestStrategy()
        public_requests = PublicRequests.view_requests(self)
       
        return self.fetch_requests_data(public_requests)


    def fetch_requests_data(self,requests):
        data_list = []
        
        for request_obj in requests:
            request_dict = request_obj.get_request_data()
            data_list.append(request_dict)

        sorted_data_list = sorted(data_list, key=lambda x:x['request_date'], reverse=True)
        return sorted_data_list
    

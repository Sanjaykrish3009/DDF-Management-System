from django.db import models
from authentication.models import CustomUser
from request.models import FundRequest
from django.db.models import Q 

class FacultyUser(CustomUser):
    faculty_id = models.CharField(max_length=30)

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


    def fetch_requests_data(self,requests):
        data_list = []
        
        for request_obj in requests:
            request_dict = request_obj.get_request_details()
            data_list.append(request_dict)

        return data_list
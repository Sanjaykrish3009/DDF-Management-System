from django.db import models
from request.models import FundRequest
from django.utils import timezone
from django.forms.models import model_to_dict

class Transaction(models.Model):
    request = models.ForeignKey(FundRequest, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    remaining_budget = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_remaining_budget(self):
        return self.remaining_budget
    
    def get_transaction_date(self):
        return self.transaction_date

    def get_transaction_details(self):
        transaction_dict = model_to_dict(self)
        transaction_dict['transaction_date'] = timezone.localtime(self.transaction_date).strftime('%Y-%m-%d %H:%M:%S')
        request_dict = model_to_dict(self.request, fields=['id','request_amount', 'transaction_type'])
        user_dict = model_to_dict(self.request.user, fields=['email'])
        request_dict['user'] = user_dict
        transaction_dict['request'] =  request_dict
        return transaction_dict
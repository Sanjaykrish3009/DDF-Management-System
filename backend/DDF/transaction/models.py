from django.db import models
from request.models import FundRequest

class Transaction(models.Model):
    request = models.ForeignKey(FundRequest, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    remaining_budget = models.DecimalField(max_digits=10, decimal_places=2)

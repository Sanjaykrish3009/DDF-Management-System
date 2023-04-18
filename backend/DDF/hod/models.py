from django.db import models
from authentication.models import CustomUser
from request.models import FundRequest
from transaction.models import Transaction
from django.db.models import Q 
from transaction.viewtransactions.hod_strategy import ViewTransactions

class HodUser(CustomUser):
    hod_id = models.CharField(max_length=30)

    def approve_request(self, request_id, hod_review):
        request_obj = FundRequest.objects.get(id=request_id)
        request_amount = request_obj.request_amount
        
        if Transaction.objects.exists():
            latest_transaction = Transaction.objects.latest('transaction_date')
            remaining_budget =  latest_transaction.get_remaining_budget()
        else:
            remaining_budget = 0.00
        
        if  request_obj.transaction_type=='Credit' or remaining_budget >= request_amount:
            request_obj.set_hod_approval(hod_review)
            return request_obj
        else:
            return None

    def disapprove_request(self, request_id, hod_review):
        fund_request = FundRequest.objects.get(id=request_id)
        fund_request.set_hod_disapproval(hod_review)

        return fund_request
    
    def view_pending_requests(self):
        pending_requests = FundRequest.objects.filter(committee_approval_status = 'Approved', hod_approval_status = 'Pending')
        return self.fetch_requests_data(pending_requests)
    
    def view_credit_requests(self):
        credit_requests = FundRequest.objects.filter(committee_approval_status = 'Approved', hod_approval_status = 'Pending', transaction_type='Credit')
        return self.fetch_requests_data(credit_requests)
    
    def view_debit_requests(self):
        debit_requests = FundRequest.objects.filter(committee_approval_status = 'Approved', hod_approval_status = 'Pending', transaction_type='Debit')
        return self.fetch_requests_data(debit_requests)
    
    def view_previous_requests(self):
        previous_requests = FundRequest.objects.exclude(Q(committee_approval_status = 'Pending') | Q(hod_approval_status = 'Pending', committee_approval_status = 'Approved'))
        return self.fetch_requests_data(previous_requests)
    
    def view_all_transactions(self):
        all_transactions = Transaction.objects.all()
        return self.fetch_transactions_data(all_transactions)
    
    def view_credit_transactions(self):
        credit_transactions = Transaction.objects.filter(request__transaction_type = 'Credit')
        return self.fetch_transactions_data(credit_transactions)
    
    def view_debit_transactions(self):
        debit_transactions = Transaction.objects.filter(request__transaction_type = 'Debit')
        return self.fetch_transactions_data(debit_transactions)
    
    def view_balance(self):
        if Transaction.objects.exists():
            latest_transaction = Transaction.objects.latest('transaction_date')
            remaining_budget =  latest_transaction.get_remaining_budget()
            return remaining_budget
        else:
            return 0.00
    
    def fetch_requests_data(self,requests):
        data_list = []
        
        for request_obj in requests:
            request_dict = request_obj.get_request_details()
            data_list.append(request_dict)

        return data_list
    
    def fetch_transactions_data(self, transactions):
        data_list = []
        
        for transaction_obj in transactions:
            transaction_dict = transaction_obj.get_transaction_details()
            data_list.append(transaction_dict)

        return data_list
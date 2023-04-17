from django.db import models
from authentication.models import CustomUser
from request.models import FundRequest
from transaction.models import Transaction
from django.db.models import Q 
from transaction.viewtransactions.committee_strategy import ViewTransactions


class CommitteeUser(CustomUser):
    committee_id = models.CharField(max_length=30)

    def approve_request(self, request_id, committee_review):
        request_obj = FundRequest.objects.get(id=request_id)
        request_amount = request_obj.request_amount
        
        if Transaction.objects.exists():
            latest_transaction = Transaction.objects.latest('transaction_date')
            remaining_budget =  latest_transaction.get_remaining_budget()
        else:
            remaining_budget = 0.00
        
        if remaining_budget >= request_amount:
            request_obj.set_committee_approval(committee_review)
            return request_obj
        else:
            return None

    def disapprove_request(self, request_id, committee_review):
        request_obj = FundRequest.objects.get(id=request_id)
        request_obj.set_committee_disapproval(committee_review)

        return request_obj
    
    def view_balance(self):
        if Transaction.objects.exists():
            latest_transaction = Transaction.objects.latest('transaction_date')
            remaining_budget =  latest_transaction.get_remaining_budget()
            return remaining_budget
        else:
            return 0.00

    def view_pending_requests(self):
        pending_requests = FundRequest.objects.filter(Q(committee_approval_status = 'Pending') | Q(user=self, hod_approval_status = 'Pending'))
        return self.fetch_requests_data(pending_requests)
    
    def view_previous_requests(self):
        previous_requests = FundRequest.objects.exclude(committee_approval_status = 'Pending')
        return self.fetch_requests_data(previous_requests)

    def view_all_transactions(self):
        all_transactions = ViewTransactions.view_all_transactions()
        return self.fetch_transactions_data(all_transactions)
    
    def view_credit_transactions(self):
        credit_transactions = ViewTransactions.view_credit_transactions()
        return self.fetch_transactions_data(credit_transactions)
    
    def view_debit_transactions(self):
        debit_transactions = ViewTransactions.view_debit_transactions()
        return self.fetch_transactions_data(debit_transactions)
    
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
    
    
    

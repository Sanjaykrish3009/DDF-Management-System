from django.db import models
from authentication.models import CustomUser
from request.models import FundRequest
from transaction.models import Transaction
from django.db.models import Q 
from transaction.viewtransactions.all_transactions_strategy import AllTransactionStrategy
from transaction.viewtransactions.credit_transactions import CreditTransactionsStrategy
from transaction.viewtransactions.debit_transactions import DebitTransactionsStrategy


class CommitteeUser(CustomUser):
    committee_id = models.CharField(max_length=30)

    def approve_request(self, request_id, committee_review):
        request_obj = FundRequest.objects.get(id=request_id)
        request_amount = request_obj.get_request_amount()
        remaining_budget = self.view_balance()
        
        if remaining_budget >= request_amount:
            request_obj = request_obj.set_committee_approval(committee_review)
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
    
    def search_view_pending_requests(self,title):
        pending_requests = FundRequest.objects.filter(Q(committee_approval_status = 'Pending') | Q(user=self, hod_approval_status = 'Pending'),request_title__icontains=title)
        return self.fetch_requests_data(pending_requests)
    
    def view_previous_requests(self):
        previous_requests = FundRequest.objects.exclude(Q(committee_approval_status = 'Pending') | Q(user=self, hod_approval_status = 'Pending'))
        return self.fetch_requests_data(previous_requests)
    
    def search_view_previous_requests(self,title):
        previous_requests = FundRequest.objects.exclude(Q(committee_approval_status = 'Pending') | Q(user=self, hod_approval_status = 'Pending'))
        previous_requests = previous_requests.filter(request_title__icontains=title)
        return self.fetch_requests_data(previous_requests)


    def view_all_transactions(self):
        AllTransactions = AllTransactionStrategy()
        all_transactions = AllTransactions.view_transactions()
        return self.fetch_transactions_data(all_transactions)
    
    def view_credit_transactions(self):
        CreditTransactions = CreditTransactionsStrategy()
        credit_transactions = CreditTransactions.view_transactions()
        return self.fetch_transactions_data(credit_transactions)
    
    def view_debit_transactions(self):
        DebitTransactions = DebitTransactionsStrategy()
        debit_transactions = DebitTransactions.view_transactions()
        return self.fetch_transactions_data(debit_transactions)
    
    def fetch_requests_data(self,requests):
        data_list = []
        
        for request_obj in requests:
            request_dict = request_obj.get_request_data()
            data_list.append(request_dict)
        sorted_data_list = sorted(data_list, key=lambda x:x['request_date'], reverse=True)

        return sorted_data_list
    
    def fetch_transactions_data(self, transactions):
        data_list = []
        
        for transaction_obj in transactions:
            transaction_dict = transaction_obj.get_transaction_details()
            data_list.append(transaction_dict)

        sorted_data_list = sorted(data_list, key=lambda x:x['request_date'], reverse=True)
        return sorted_data_list
    
    
    

from decimal import Decimal
from django.db import models
import pandas as pd
from django.core.mail import EmailMessage
from authentication.models import CustomUser
from request.models import FundRequest
from transaction.models import Transaction
from django.db.models import Q 
from transaction.viewtransactions.all_transactions_strategy import AllTransactionStrategy
from transaction.viewtransactions.credit_transactions import CreditTransactionsStrategy
from transaction.viewtransactions.debit_transactions import DebitTransactionsStrategy

class HodUser(CustomUser):
    hod_id = models.CharField(max_length=30)

    def approve_request(self, request_id, hod_review):
        request_obj = FundRequest.objects.get(id=request_id)
        request_amount = request_obj.get_request_amount()
        transaction_type = request_obj.get_transaction_type()   
        remaining_budget = self.view_balance()

        if  transaction_type =='Debit' and remaining_budget < request_amount:
            return None

        request_obj.set_hod_approval(hod_review)

        if transaction_type == 'Debit':
            remaining_budget -= request_amount
        else:
            remaining_budget += request_amount

        transaction = Transaction(request=request_obj,remaining_budget=remaining_budget)
        transaction.save()
        
        return transaction

    def disapprove_request(self, request_id, hod_review):
        fund_request = FundRequest.objects.get(id=request_id)
        fund_request.set_hod_disapproval(hod_review)

        return fund_request
    
    def view_pending_requests(self):
        pending_requests = FundRequest.objects.filter(committee_approval_status = 'Approved', hod_approval_status = 'Pending')
        return self.fetch_requests_data(pending_requests)
    
    def search_view_pending_requests(self,title):
        pending_requests = FundRequest.objects.filter(committee_approval_status = 'Approved', hod_approval_status = 'Pending',request_title__icontains=title)
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
    
    def search_view_previous_requests(self,title):
        previous_requests = FundRequest.objects.exclude(Q(committee_approval_status = 'Pending') | Q(hod_approval_status = 'Pending', committee_approval_status = 'Approved'))
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
        Debit_transactions = DebitTransactionsStrategy()
        debit_transactions = Debit_transactions.view_transactions()
        return self.fetch_transactions_data(debit_transactions)
    
    def view_balance(self):
        if Transaction.objects.exists():
            latest_transaction = Transaction.objects.latest('transaction_date')
            remaining_budget =  latest_transaction.get_remaining_budget()
            return remaining_budget
        else:
            return Decimal(0.00)
    
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

        sorted_data_list = sorted(data_list, key=lambda x:x['transaction_date'], reverse=False)

        return sorted_data_list
    
    def send_excel(self):
        transactions_list = self.view_all_transactions()
        df = pd.DataFrame(transactions_list)
               
        df = pd.DataFrame({'ID': transaction['id'],
                            'Request ID': transaction['request']['id'],
                            'Amount': transaction['request']['request_amount'],
                            'Type': transaction['request']['transaction_type'],
                            'Requested By': transaction['request']['user']['email'],
                            'Date and Time': transaction['transaction_date'],
                            'Balance': str(transaction['remaining_budget'])
                        } for transaction in transactions_list)
                
        excel_file = pd.ExcelWriter('ddf-transactions.xlsx')
        df.to_excel(excel_file, index=False)
        excel_file.save()

        subject = 'DDF Account Transactions Update'
        message = f'Please find attached the Transactions Data Excel sheet.'
        from_email = 'ddf.cse.iith@gmail.com' 
        recipient_list = ['cs19btech11022@iith.ac.in']
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.attach_file('ddf-transactions.xlsx')
        email.send()
       
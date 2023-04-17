from .viewtransactions_strategy import ViewTransactionsStrategy
from transaction.models import Transaction

class ViewTransactions(ViewTransactionsStrategy):

    def view_all_transactions(self):
        all_transactions = Transaction.objects.all()
        return self.fetch_transactions_data(all_transactions)
    
    def view_credit_transactions(self):
        credit_transactions = Transaction.objects.filter(request__transaction_type = 'Credit')
        return self.fetch_transactions_data(credit_transactions)
    
    def view_debit_transactions(self):
        debit_transactions = Transaction.objects.filter(request__transaction_type = 'Debit')
        return self.fetch_transactions_data(debit_transactions)
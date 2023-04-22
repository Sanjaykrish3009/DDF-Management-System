from .viewtransactions_strategy import ViewTransactionsStrategy
from transaction.models import Transaction

class DebitTransactionsStrategy(ViewTransactionsStrategy):
    
    def view_transactions(self):
        debit_transactions = Transaction.objects.filter(request__transaction_type = 'Debit')
        return debit_transactions
    

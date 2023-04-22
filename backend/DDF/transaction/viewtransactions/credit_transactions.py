from .viewtransactions_strategy import ViewTransactionsStrategy
from transaction.models import Transaction

class CreditTransactionsStrategy(ViewTransactionsStrategy):
    
    def view_transactions(self):
        credit_transactions = Transaction.objects.filter(request__transaction_type = 'Credit')
        return credit_transactions
    

from .viewtransactions_strategy import ViewTransactionsStrategy
from transaction.models import Transaction

class AllTransactionStrategy(ViewTransactionsStrategy):

    def view_transactions(self):
        all_transactions = Transaction.objects.all()
        return all_transactions
    
 
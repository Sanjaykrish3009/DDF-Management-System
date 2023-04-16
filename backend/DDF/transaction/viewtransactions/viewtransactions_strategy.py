from abc import ABC, abstractmethod

class ViewTransactionsStrategy(ABC):
    
    @abstractmethod
    def view_all_transactions(self):
        pass
    
    @abstractmethod
    def view_credit_transactions(self):
        pass

    @abstractmethod
    def view_debit_transactions(self):
        pass
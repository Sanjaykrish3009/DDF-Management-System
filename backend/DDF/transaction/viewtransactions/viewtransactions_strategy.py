from abc import ABC, abstractmethod

class ViewTransactionsStrategy(ABC):
    
    @abstractmethod
    def view_transactions(self):
        pass

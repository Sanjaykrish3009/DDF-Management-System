from .viewtransactions_strategy import ViewTransactionsStrategy

class ContextTransaction:
    def __init__(self,strategy:ViewTransactionsStrategy) -> None:
        self._startegy = strategy

    def get_strategy(self) ->None:
        return self._startegy
    

    def set_strategy(self,strategy:ViewTransactionsStrategy)->None:
        self._startegy = strategy

    def view_transactions(self):
        return self._startegy.view_transactions()

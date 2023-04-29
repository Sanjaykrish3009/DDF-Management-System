from .viewrequests_strategy import ViewRequestsStrategy

class ContextRequest:
    def __init__(self,strategy:ViewRequestsStrategy) -> None:
        self._startegy = strategy

    def get_strategy(self) ->None:
        return self._startegy
    

    def set_strategy(self,strategy:ViewRequestsStrategy)->None:
        self._startegy = strategy

    def view_requests(self,user):
        return self._startegy.view_requests(user)
    

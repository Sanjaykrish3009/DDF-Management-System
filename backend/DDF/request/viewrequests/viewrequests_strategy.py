from abc import ABC, abstractmethod

class ViewRequestsStrategy(ABC):
    
    @abstractmethod
    def view_requests(self,user):
        pass



    

    
    
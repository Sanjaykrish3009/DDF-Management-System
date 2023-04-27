from abc import ABC, abstractmethod

class ViewRequestsStrategy(ABC):
    
    @abstractmethod
    def view_requests(self,user):
        pass

    @abstractmethod
    def search_view_requests(self,user,title):
        pass



    

    
    
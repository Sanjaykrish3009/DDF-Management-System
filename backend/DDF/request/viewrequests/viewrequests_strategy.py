from abc import ABC, abstractmethod

# class ViewRequestsStrategy(ABC):
    
#     @abstractmethod
#     def view_pending_requests(self):
#         pass
    
#     @abstractmethod
#     def view_previous_requests(self):
#         pass
    
#     @abstractmethod
#     def view_public_requests(self):
#         pass
    
class ViewRequestsStrategy(ABC):
    
    @abstractmethod
    def view_requests(self,user):
        pass



    

    
    
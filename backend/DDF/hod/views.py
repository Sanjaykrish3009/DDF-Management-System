from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HodUser

class PendingRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.query_params

        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            if 'title' in data and data['title'].isspace()==False:
                pending_requests = hod_user.search_view_pending_requests(data['title'])
            else:
                pending_requests = hod_user.view_pending_requests()
            return Response({'success':'Pending requests of hod retrieved successfully', 'data':pending_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the pending requests of the hod'})

class CreditRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            credit_requests = hod_user.view_credit_requests()
            return Response({'success':'Credit requests retrieved successfully', 'data':credit_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the credit requests'})
        
class DebitRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            debit_requests = hod_user.view_debit_requests()
            return Response({'success':'Debit requests of hod retrieved successfully', 'data':debit_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the debit requests'})
        
class PreviousRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.query_params

        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            if 'title' in data and data['title'].isspace()==False:
                previous_requests = hod_user.search_view_previous_requests(data['title'])
            else:
                previous_requests = hod_user.view_previous_requests()
            return Response({'success':'Previous requests of hod retrieved successfully', 'data':previous_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the previous requests of the hod'})


class Approval(APIView):
    def post(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.data

        if 'request_id' not in data:
            return Response({'error':'Request ID field must be set'})
        
        if 'hod_review' not in data or data['hod_review']=='':
            return Response({'error': 'HOD Review field must be set'})
        
        request_id = data['request_id']
        hod_review = data['hod_review']

        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            transaction = hod_user.approve_request(request_id, hod_review)
            if transaction:
                return Response({'success':'Fund request approved by the hod successfully'})
            else:
                return Response({'error': 'Request amount more than remaining budget'})
        except:
            return Response({'error':'Something went wrong while approving fund request by the hod'})

class Disapproval(APIView):
    def post(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.data

        if 'request_id' not in data:
            return Response({'error': 'Request ID field must be set'})
        
        if 'hod_review' not in data or data['committee_review'].isspace():
            return Response({'error': 'HOD Review field must be set'})
        
        request_id = data['request_id']
        hod_review = data['hod_review']
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            hod_user.disapprove_request(request_id,hod_review)
            return Response({'success':'Fund request disapproved by the hod successfully'})
        except:
            return Response({'error':'Something went wrong while disapproving fund request by the hod'})

class AllTransactions(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            all_transactions = hod_user.view_all_transactions()
            return Response({'success':'All transactions retrieved successfully by the hod', 'data':all_transactions})
        except:
            return Response({'error':'Something went wrong while retrieving all transactions by the hod'})
        
class CreditTransactions(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            credit_transactions = hod_user.view_credit_transactions()
            return Response({'success':'Credit transactions retrieved successfully by the hod', 'data':credit_transactions})
        except:
            return Response({'error':'Something went wrong while retrieving credit transactions'})

class DebitTransactions(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            debit_transactions = hod_user.view_debit_transactions()
            return Response({'success':'Debit transactions retrieved successfully by the hod', 'data':debit_transactions})
        except:
            return Response({'error':'Something went wrong while retrieving debit transactions'})

class Balance(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            balance = hod_user.view_balance()
            return Response({'success':'Balance viewed successfully', 'data':balance})
        except:
            return Response({'error':'Something went wrong while viewing balance'})
        

class SendExcelSheet(APIView):    
    def get(self,request,format=None): 
        user = self.request.user
        email = user.email
        try:
            hod_user = HodUser.objects.filter(email=email)[0]
            hod_user.send_excel()
            return Response({'success':'Excel Sheet sent to admin'})
        except:
            return Response({'error':'Something went wrong while sending excel sheet to admin'})


  

                
    

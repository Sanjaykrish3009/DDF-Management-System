from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CommitteeUser

class PendingRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.query_params

        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            if 'title' in data:
                pending_requests = committee_user.search_view_pending_requests(data['title'])
            else:
                pending_requests = committee_user.view_pending_requests()
            return Response({'success':'Pending requests of committee retrieved successfully', 'data':pending_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the pending requests of the committee'})

class PreviousRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        data = self.request.query_params

        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            if 'title' in data:
                previous_requests = committee_user.search_view_previous_requests(data['title'])

            else:
                previous_requests = committee_user.view_previous_requests()
            return Response({'success':'Previous requests of committee retrieved successfully', 'data':previous_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the previous requests of the committee'})

class Approval(APIView):
    def post(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.data

        if 'request_id' not in data:
            return Response({'error': 'Request ID field must be set'})
        
        if 'committee_review' not in data or data['committee_review']=='':
            return Response({'error': 'Committee Review field must be set'})
        
        request_id = data['request_id']
        committee_review = data['committee_review']
        

        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            if committee_user.approve_request(request_id, committee_review):
                return Response({'success':'Fund request approved by the committee successfully'})
            else:
                return Response({'error': 'Request amount more than remaining budget'})
        except:
            return Response({'error':'Something went wrong while approving fund request by the committee'})

class Disapproval(APIView):
    def post(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.data

        if 'request_id' not in data:
            return Response({'error': 'Request ID field must be set'})
        
        if 'committee_review' not in data or data['committee_review']=='':
            return Response({'error': 'Committee Review field must be set'})
        
        request_id = data['request_id']
        committee_review = data['committee_review']
        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            committee_user.disapprove_request(request_id,committee_review)
            return Response({'success':'Fund request disapproved by the committee successfully'})
        except:
            return Response({'error':'Something went wrong while disapproving fund request by the committee'})

class AllTransactions(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            all_transactions = committee_user.view_all_transactions()
            return Response({'success':'All transactions retrieved successfully by the committee', 'data':all_transactions})
        except:
            return Response({'error':'Something went wrong while retrieving all transactions by the committee'})
        
class CreditTransactions(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            credit_transactions = committee_user.view_credit_transactions()
            return Response({'success':'Credit transactions retrieved successfully by the hod', 'data':credit_transactions})
        except:
            return Response({'error':'Something went wrong while retrieving credit transactions'})

class DebitTransactions(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            debit_transactions = committee_user.view_debit_transactions()
            return Response({'success':'Debit transactions retrieved successfully by the hod', 'data':debit_transactions})
        except:
            return Response({'error':'Something went wrong while retrieving debit transactions'})
        
class Balance(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
  
        try:
            committee_user = CommitteeUser.objects.filter(email=email)[0]
            balance = committee_user.view_balance()
            return Response({'success':'Balance viewed successfully', 'data':balance})
        except:
            return Response({'error':'Something went wrong while viewing balance'})
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from request.models import FundRequest
from decimal import Decimal

class CreateTransaction(APIView):
    def post(self, request, format=None):
        data = self.request.data
        request_id = data['request_id']
        request_obj = FundRequest.objects.get(id=request_id)
        request_amount = request_obj.request_amount

        try:
            if Transaction.objects.exists()==False:
                remaining_budget = Decimal(0.00)
            else:
                latest_transaction = Transaction.objects.latest('transaction_date')
                remaining_budget = latest_transaction.get_remaining_budget()
            
            if request_obj.transaction_type == 'Debit':
                remaining_budget -= request_amount
            else:
                remaining_budget += request_amount

            transaction = Transaction(request=request_obj,remaining_budget=remaining_budget)
            transaction.save()
        
            return Response({'success':'Transaction created successfully'})
        except:
            return Response({'error':'Something went wrong while creating Transaction'})
        
class TransactionDetails(APIView):
    def get(self, request, format=None):
        data = self.request.data
        transaction_id = data['transaction_id']

        try:
            transaction_obj = Transaction.objects.get(id=transaction_id)
            transaction_dict = transaction_obj.get_transaction_details()
            return Response({'success':'Transaction viewed successfully', 'data': transaction_dict})
        except:
            return Response({'error':'Something went wrong while viewing Transaction'})
    

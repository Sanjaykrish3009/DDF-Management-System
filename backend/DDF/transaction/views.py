from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction

class TransactionDetails(APIView):
    def post(self, request, format=None):
        data = self.request.data

        if 'transaction_id' not in data:
            raise ValueError('Transaction ID field must be set')
        
        transaction_id = data['transaction_id']

        try:
            transaction_obj = Transaction.objects.get(id=transaction_id)
            transaction_dict = transaction_obj.get_transaction_details()
            return Response({'success':'Transaction viewed successfully', 'data': transaction_dict})
        except:
            return Response({'error':'Something went wrong while viewing Transaction'})


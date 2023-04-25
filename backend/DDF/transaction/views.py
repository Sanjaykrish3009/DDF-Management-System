from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction

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

# class GenerateExcel(APIView):
    
    def post(self,request,format=None):
        # Get the data from the database
        queryset = Transaction.objects.all()
        
        # Get the desired column names
        column_names = ['id', '', 'phone']
        
        # Create the Excel sheet and add the column names
        wb = Workbook()
        ws = wb.active
        ws.append(column_names)
        
        # Add the data to the Excel sheet
        for obj in queryset:
            row_data = [getattr(obj, col_name) for col_name in column_names]
            ws.append(row_data)

        # Save the Excel sheet
        excel_file_path = 'my_data.xlsx'
        wb.save(excel_file_path)

        # Send the Excel sheet as an attachment
        email = EmailMessage(
            'My Data Excel Sheet',
            'Please find attached the My Data Excel sheet.',
            'from@example.com',
            ['to@example.com']
        )
        email.attach_file(excel_file_path)
        email.send()

        # Return a response to the client
        response = sendfile(request, excel_file_path, attachment=True)
        return response
            
    

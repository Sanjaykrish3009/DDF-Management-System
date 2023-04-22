import os
from django.http import FileResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from DDF.settings import MEDIA_ROOT
from .models import FundRequest

    
class CreatePrivateFundRequest(APIView):
    def post(self,request,format=None):
        data = self.request.data
        user = self.request.user
        request_type = "PrivateRequest"
        request_title = data['request_title']
        request_description = data['request_description']
        request_amount = data['request_amount']

        try:
            fund_request = FundRequest(user=user, request_type=request_type, request_title=request_title, 
                            request_description=request_description, request_amount=request_amount)
            fund_request.save()
            return Response({'success':'Private Fund Request created successfully'})
        except:
            return Response({'error':'Something went wrong while creating Private Fund Request'})


class CreatePublicFundRequest(APIView):
    def post(self,request,format=None):
        data = self.request.data
        user = self.request.user
        request_type = "PublicRequest"
        request_title = data['request_title']
        request_description = data['request_description']
        request_amount = data['request_amount']
        file = self.request.FILES.get('file')

        try:
            fund_request = FundRequest(user=user, request_type=request_type, request_title=request_title, 
                            request_description=request_description, request_amount=request_amount, upload=file)
            fund_request.save()
            return Response({'success':'Public Fund Request created successfully'})
        except:
            return Response({'error':'Something went wrong while creating Public Fund Request'})

class CreateBudgetRequest(APIView):
    def post(self,request,format=None):
        data = self.request.data
        user = self.request.user
        request_type = "PrivateRequest"
        request_title = data['request_title']
        request_description = data['request_description']
        request_amount = data['request_amount']
        transaction_type = "Credit"
        

        try:
            fund_request = FundRequest(user=user, request_type=request_type, request_title=request_title, 
                            request_description=request_description, request_amount=request_amount, transaction_type=transaction_type,committee_approval_status=True)
            fund_request.save()
            return Response({'success':'Budget Request created successfully'})
        except:
            return Response({'error':'Something went wrong while creating Private Fund Request'})

class RequestDetails(APIView):
    def get(self, request, format=None):
        data = self.request.data
        request_id = data['request_id']

        try:
            request_obj = FundRequest.objects.get(id=request_id)
            request_dict = request_obj.get_request_details()
            return Response({'success':'Fund request viewed successfully', 'data': request_dict})
        except:
            return Response({'error':'Something went wrong while viewing fund request'})

class FileDetails(APIView):
    def get(self, request, format=None):
        data = self.request.data
        file_path = data['file_path']
        file_path = os.path.join(MEDIA_ROOT, file_path)
        
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        else:
            raise Http404("File not found")

import mimetypes
import os
from django.http import FileResponse, Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from DDF.settings import MEDIA_ROOT
from .models import FundRequest
    
class CreatePrivateFundRequest(APIView):
    def post(self,request,format=None):
        data = self.request.data
        user = self.request.user

        if 'request_title' not in data:
            return Response({'error': 'Request Title field must be set'})
        
        if 'request_description' not in data:
            return Response({'error': 'Request Description field must be set'})
        
        if 'request_amount' not in data:
            return Response({'error': 'Request Amount field must be set'})
        
        request_type = "PrivateRequest"        
        request_title = data['request_title']
        request_description = data['request_description']
        request_amount = data['request_amount']
        file = self.request.FILES.get('file')
        
        try:
            fund_request = FundRequest(user=user, request_type=request_type, request_title=request_title, 
                            request_description=request_description, request_amount=request_amount,upload=file)
            fund_request.save()
            return Response({'success':'Private Fund Request created successfully'})
        except:
            return Response({'error':'Something went wrong while creating Private Fund Request'})


class CreatePublicFundRequest(APIView):
    def post(self,request,format=None):
        data = self.request.data
        user = self.request.user
        
        if 'request_title' not in data:
            return Response({'error': 'Request Title field must be set'})
        
        if 'request_description' not in data:
            return Response({'error': 'Request Description field must be set'})
        
        if 'request_amount' not in data:
            return Response({'error': 'Request Amount field must be set'})
        
        request_type = "PublicRequest"
        request_title = data['request_title']
        request_description = data['request_description']
        request_amount = data['request_amount']
        file = self.request.FILES.get('file')

        if file is None:
            return Response({'error': 'File must be uploaded for public request'})

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

        if 'request_title' not in data:
            return Response({'error': 'Request Title field must be set'})
        
        if 'request_description' not in data:
            return Response({'error': 'Request Description field must be set'})
        
        if 'request_amount' not in data:
            return Response({'error': 'Request Amount field must be set'})

        request_type = "PrivateRequest"
        request_title = data['request_title']
        request_description = data['request_description']
        request_amount = data['request_amount']
        transaction_type = "Credit"
        file = self.request.FILES.get('file')

        try:
            fund_request = FundRequest(user=user, request_type=request_type, request_title=request_title, 
                            request_description=request_description, request_amount=request_amount, transaction_type=transaction_type,committee_approval_status='Approved', upload=file)
            fund_request.save()
            return Response({'success':'Budget Request created successfully'})
        except:
            return Response({'error':'Something went wrong while creating Private Fund Request'})

class RequestDetails(APIView):
    def post(self, request, format=None):
        data = self.request.data
        if 'request_id' not in data:
            return Response({'error': 'Request ID field must be set'})
        
        request_id = data['request_id']

        try:
            request_obj = FundRequest.objects.get(id=request_id)
            request_dict = request_obj.get_request_details()
            return Response({'success':'Fund request viewed successfully', 'data': request_dict})
        except:
            return Response({'error':'Something went wrong while viewing fund request'})

class FileDetails(APIView):
    def get(self, request, format=None):
        data = self.request.query_params

        if 'file_path' not in data:
            return Response({'error': 'File Path field must be set'})
        
        file_path = data['file_path']
        file_path = os.path.join(MEDIA_ROOT, file_path)
        
        if os.path.exists(file_path):
            file_type, _ = mimetypes.guess_type(file_path)
            if file_type is None:
                return HttpResponse(status=500)
            file = open(file_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = file_type
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_path.split('/')[-1])
            return response
        else:
            raise Http404("File not found")

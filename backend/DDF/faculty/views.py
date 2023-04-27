from rest_framework.views import APIView
from rest_framework.response import Response
from faculty.models import FacultyUser

class PendingRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.query_params

        try:
            faculty_user = FacultyUser.objects.get(email=email)

            if 'title' in data:
                pending_requests = faculty_user.search_view_pending_requests(data['title'])
            else:
                pending_requests = faculty_user.view_pending_requests()
            return Response({'success':'Pending requests of faculty retrieved successfully', 'data':pending_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the pending requests of the faculty'})
        
class PreviousRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.query_params

  
        try:
            faculty_user = FacultyUser.objects.get(email=email)

            if 'title' in data:
                previous_requests = faculty_user.search_view_previous_requests(data['title'])
            else:
                previous_requests = faculty_user.view_previous_requests()
            return Response({'success':'Previous requests of faculty retrieved successfully', 'data': previous_requests})
        except:
            return Response({'error':'Something went wrong while retrieving the previous requests'})

class PublicRequests(APIView):
    def get(self, request, format=None):
        user = self.request.user
        email = user.email
        data = self.request.query_params

  
        try:
            faculty_user = FacultyUser.objects.get(email=email)
            if 'title' in data:
                public_requests = faculty_user.search_view_public_requests(data['title'])

            else:
                public_requests = faculty_user.view_public_requests()
            return Response({'success':'All public requests of faculties retrieved successfully', 'data': public_requests})
        except:
            return Response({'error':'Something went wrong while retrieving all public requests'})     

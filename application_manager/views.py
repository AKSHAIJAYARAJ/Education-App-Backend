from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationManagerSerializer
from .application_manager import ApplicationManager
from education.paginator import PaginatedView


class ApplicationManagerViewSet(APIView):
    
    validator = ApplicationManagerSerializer
    
    def post(self,request):
        try:
            application = self.validator(data=request.data,context={'request': self.request})
            if application.is_valid():
                response = ApplicationManager().post(payload = application.validated_data)
                return Response(data={"status":'OK',"result":'application created','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": application.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        application_id = request.query_params.get("application_id")
        try:
            if application_id:
                response = ApplicationManager().get(filters= {'application_id':application_id})
                return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
            else:
                response = ApplicationManager().get()
                paginator = PaginatedView()
                paginated_queryset = paginator.paginate_queryset(response, request)
                serializer = ApplicationManagerSerializer(paginated_queryset, many=True)
                return paginator.get_paginated_response(serializer.data)

        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        application_id = request.query_params.get("application_id")
        try:
            application = self.validator(data=request.data,context={'request': self.request})
            if application.is_valid():
                response = ApplicationManager().put(payload = application.validated_data,application_id=application_id)
                return Response(data={"status":'OK',"result":'application updated','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": application.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        application_id = request.query_params.get("application_id")
        try:
        
            response = ApplicationManager().delete(application_id=application_id)
            return Response(data={"status":'OK',"result":'application deleted','message':"SUCCESS"},status=status.HTTP_200_OK)
       
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

# class AdminAppliedCourseDetailsViewSet(APIView):
    

#     def get(self,request):
#         application_id = request.query_params.get("application_id")
#         try:
#             if application_id:
#                 response = ApplicationManager().get(filters= {'application_id':application_id})
#                 return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
#             else:
#                 response = ApplicationManager().get()
#                 paginator = PaginatedView()
#                 paginated_queryset = paginator.paginate_queryset(response, request)
#                 serializer = ApplicationManagerSerializer(paginated_queryset, many=True)
#                 return paginator.get_paginated_response(serializer.data)

#         except Exception as e:
#             print("-----EPTN----",e)
#             return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

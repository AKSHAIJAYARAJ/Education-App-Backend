from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseManagerSerializer
from .course_manager import CourseManager
from education.paginator import PaginatedView


class CourseManagerViewSet(APIView):
    
    validator = CourseManagerSerializer
    
    def post(self,request):
        try:
            course = self.validator(data=request.data,context={'request': self.request})
            if course.is_valid():
                response = CourseManager().post(payload = course.validated_data)
                return Response(data={"status":'OK',"result":'course created','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": course.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        course_id = request.query_params.get("course_id")
        try:
            response = CourseManager().get(filters= {'course_id':course_id})
            return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        course_id = request.query_params.get("course_id")
        try:
            course = self.validator(data=request.data,context={'request': self.request})
            if course.is_valid():
                response = CourseManager().put(payload = course.validated_data,course_id=course_id)
                return Response(data={"status":'OK',"result":'course updated','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": course.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        course_id = request.query_params.get("course_id")
        try:
        
            response = CourseManager().delete(course_id=course_id)
            return Response(data={"status":'OK',"result":'course deleted','message':"SUCCESS"},status=status.HTTP_200_OK)
       
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

class UserCourseDetailsViewSet(APIView):
    

    def get(self,request):
        course_id = request.query_params.get("course_id")
        try:
            if course_id:
                response = CourseManager().get(filters= {'course_id':course_id})
                return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
            else:
                response = CourseManager().get()
                paginator = PaginatedView()
                paginated_queryset = paginator.paginate_queryset(response, request)
                serializer = CourseManagerSerializer(paginated_queryset, many=True)
                return paginator.get_paginated_response(serializer.data)

        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

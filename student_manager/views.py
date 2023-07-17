from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentManagerSerializer
from .student_manager import Student

class StudentManagerViewSet(APIView):

    validator = StudentManagerSerializer

    def post(self,request):
        try:
            student = self.validator(data=request.data)
            if student.is_valid:
                response = Student().post(payload = student.validated_data)
                return Response(data={"status":'OK',"result":'student created','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": student.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        student_id = request.query_params.get("student_id")
        try:
            response = Student().get(filters= {'student_id':student_id})
            return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        student_id = request.query_params.get("student_id")
        try:
            student = self.validator(data=request.data)
            if student.is_valid:
                response = Student().put(payload = student.validated_data,student_id=student_id)
                return Response(data={"status":'OK',"result":'student updated','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": student.errors,'message':"Invalid"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        student_id = request.query_params.get("student_id")
        try:
        
            response = Student().delete(student_id=student_id)
            return Response(data={"status":'OK',"result":'student deleted','message':"SUCCESS"},status=status.HTTP_200_OK)
       
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

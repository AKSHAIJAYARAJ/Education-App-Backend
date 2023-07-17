from .models import StudentModel

class Student:
    student = StudentModel
    def get(self,filters:dict = None):
        
        try:
            instance = self.student.objects.filter(**filters).all()
            user_data = list(instance.values())
            return user_data
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def post(self,payload : dict = None):
        try:
            instance = self.student(**payload)
            instance.save()
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def put(self,payload : dict, student_id : int):
        try:
            instance = self.student.objects.get(student_id = student_id)
            for key, value in payload.items():
                setattr(instance, key, value)
            instance.save()
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def delete(self,student_id : int):
        try:
            instance = self.student.objects.get(student_id = student_id)
            instance.delete()
            
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
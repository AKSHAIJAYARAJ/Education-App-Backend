from .models import ApplicationModel

class ApplicationManager:
    course = ApplicationModel
    def get(self,filters:dict = None):
        
        try:
            if filters:
                instance = self.course.objects.filter(**filters).all()
                user_data = list(instance.values())
            else:
                user_data = self.course.objects.all()
            return user_data
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def post(self,payload : dict = None):
        try:
            instance = self.course(**payload)
            instance.save()
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def put(self,payload : dict, application_id : int):
        try:
            instance = self.course.objects.get(application_id = application_id)
            for key, value in payload.items():
                setattr(instance, key, value)
            instance.save()
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
    def delete(self,application_id : int):
        try:
            instance = self.course.objects.get(application_id = application_id)
            instance.delete()
            
            return True
        except Exception as e:
            print("-----User EPTN-------",e)
            return False
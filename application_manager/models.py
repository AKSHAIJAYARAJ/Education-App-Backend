from django.db import models

# Create your models here.
class ApplicationModel(models.Model):
    
    application_id = models.AutoField(primary_key=True,unique=True)
    student_id = models.CharField(max_length=200,null=True,blank=True)
    course_id = models.CharField(max_length=200,null=True,blank=True)
    payment_status = models.CharField(max_length=20,null=True,blank=True)
    applied_on = models.DateTimeField(auto_now=True,null=True,blank=True)
    preferred_exam_date = models.DateTimeField(null=True,blank=True)
    exam_status = models.CharField(max_length=20,null=True,blank=True)
    application_status = models.CharField(max_length=10,null=True,blank=True)
   
from django.db import models

# Create your models here.

class StudentModel(models.Model):

    student_id = models.AutoField(primary_key=True,unique=True)
    student_uuid = models.CharField(max_length=200,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    preference = models.JSONField(null=True,blank=True)
    
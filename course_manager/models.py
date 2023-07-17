from django.db import models

# Create your models here.

class CourseModel(models.Model):
    
    course_id = models.AutoField(primary_key=True,unique=True)
    course_name = models.CharField(max_length=200,null=True,blank=True)
    course_description = models.CharField(max_length=200,null=True,blank=True)
    course_rating = models.FloatField(null=True,blank=True)
    course_price = models.FloatField(null=True,blank=True)
    course_discount = models.FloatField(null=True,blank=True)
    course_status = models.CharField(max_length=10,null=True,blank=True)
   
    

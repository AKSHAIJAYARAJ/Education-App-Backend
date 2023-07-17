from django.db import models
import uuid

# Create your models here.
class UserModel(models.Model):
    
    user_id = models.AutoField(primary_key=True,unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user_phone_number = models.CharField(max_length=13,null=True,blank=True)
    user_email = models.CharField(max_length=150,null=True,blank=True)
    user_password = models.CharField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    modified_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user_is_active = models.BooleanField(default=True,null=True,blank=True)
    role = models.CharField(max_length=13,null=True,blank=True,default='student')

    def __str__(self):
        return str(self.uuid)
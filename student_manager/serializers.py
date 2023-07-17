from rest_framework.serializers import ModelSerializer
from .models import StudentModel


class StudentManagerSerializer(ModelSerializer):

    class Meta:
        model = StudentModel
        fields = "__all__"
from rest_framework.serializers import ModelSerializer
from .models import CourseModel


class CourseManagerSerializer(ModelSerializer):

    class Meta:
        model = CourseModel
        fields = "__all__"
from rest_framework.serializers import ModelSerializer
from .models import ApplicationModel


class ApplicationManagerSerializer(ModelSerializer):

    class Meta:
        model = ApplicationModel
        fields = "__all__"
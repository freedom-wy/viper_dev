from rest_framework.serializers import ModelSerializer
from .models import HostModel


class HostSerializer(ModelSerializer):
    class Meta(object):
        model = HostModel
        fields = "__all__"

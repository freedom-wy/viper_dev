from rest_framework.serializers import ModelSerializer
from .models import HostModel
from rest_framework.serializers import Serializer, IntegerField, DictField, CharField


class HostSerializer(ModelSerializer):
    class Meta(object):
        model = HostModel
        fields = "__all__"


class PortServiceSerializer(Serializer):
    ipaddress = CharField(max_length=100)
    update_time = IntegerField()
    port = IntegerField()
    banner = DictField()
    service = CharField(max_length=100)

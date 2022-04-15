from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer


class FakeSerializer(Serializer):
    pass


class BaseView(ModelViewSet, UpdateAPIView, DestroyAPIView):
    queryset = None
    serializer_class = FakeSerializer

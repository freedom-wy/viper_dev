from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


class BaseView(ModelViewSet, UpdateAPIView, DestroyAPIView):
    queryset = None
    serializer_class = None

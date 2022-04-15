from django.shortcuts import render
from utils.base_views import BaseView
from rest_framework.response import Response
from rest_framework import status
from .models import HostModel
from .serializers import HostSerializer


# Create your views here.

class HostView(BaseView):
    # queryset = HostModel.objects.all()
    # serializer_class = HostSerializer
    def list(self, request, *args, **kwargs):
        data = Host.list()
        return Response(data=data, status=status.HTTP_200_OK)

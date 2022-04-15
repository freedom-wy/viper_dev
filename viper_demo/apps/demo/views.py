from django.shortcuts import render
from utils.base_views import BaseView
from rest_framework.response import Response
from rest_framework import status
from Handle.handle import Handle
from Handle.host import Host
import json


# Create your views here.

class HostView(BaseView):
    """
    查看主机数据
    """
    def list(self, request, *args, **kwargs):
        data = Host.list()
        return Response(data=data, status=status.HTTP_200_OK)


class HandleView(BaseView):
    """
    添加监听
    """
    def create(self, request, *args, **kwargs):
        opts = request.data.get("opts")
        if isinstance(opts, str):
            opts = json.loads(opts)
        # 根据前端传递的参数创建监听
        context = Handle.create(opts)
        return Response(data=context, status=status.HTTP_200_OK)

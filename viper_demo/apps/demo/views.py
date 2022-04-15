from utils.log import logger
from utils.base_views import BaseView
from rest_framework.response import Response
from rest_framework import status
from Handle.handle import Handle
from Handle.host import Host
import json
from Handle.payload import Payload


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


class PayloadView(BaseView):
    """
    生成payload
    """
    def create(self, request, *args, **kwargs):
        logger.info("前端传递数据为: {}".format(request.data))
        mname = request.data.get("mname")
        opts = request.data.get("opts")
        if isinstance(opts, str):
            opts = json.loads(opts)
        response = Payload.create(mname, opts)
        # return Response(data=byteresult, content_type='application/octet-stream', status=status.HTTP_200_OK)
        return response

# Create your views here.

# import json

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Lib.api import data_return
from Lib.baseview import BaseView
from Lib.configs import *
from Lib.log import logger


class TheHiveView(BaseView):
    permission_classes = (AllowAny,)  # 无需认证

    def create(self, request, **kwargs):
        try:
            logger.info(request.data)
            context = data_return(200, {}, CODE_MSG_ZH.get(200), CODE_MSG_EN.get(200))
            return Response(context)
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
            return Response(context)

from utils.log import logger
from utils.base_views import BaseView
from rest_framework.response import Response
from rest_framework import status
from Handle.handle import Handle
from Handle.host import Host
import json
from Handle.payload import Payload
from Handle.session import Session
from Handle.postmoduleactuator import PostModuleActuator
from utils.xcache import Xcache


# Create your views here.
class SessionView(BaseView):
    def list(self, request, *args, **kwargs):
        """
        查看session信息
        """
        data = Session.list()
        return Response(data=data, status=status.HTTP_200_OK)


class HostView(BaseView):
    """
    查看主机数据
    """

    def list(self, request, *args, **kwargs):
        data = Host.list()
        return Response(data=data, status=status.HTTP_200_OK)


class HandleView(BaseView):

    def list(self, request, *args, **kwargs):
        """
        监听列表
        """
        context = Handle.list()
        return Response(data=context, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        创建监听
        """
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

    # def list(self, request, *args, **kwargs):
    #     data = {'mname': 'windows/x64/meterpreter/reverse_tcp', 'opts': {'PAYLOAD': 'windows/x64/meterpreter/reverse_tcp', 'WORKSPACE': None, 'VERBOSE': False, 'WfsDelay': 2, 'EnableContextEncoding': False, 'ContextInformationFile': None, 'DisablePayloadHandler': False, 'ExitOnSession': False, 'ListenerTimeout': 0, 'LHOST': '172.16.171.129', 'LPORT': 1234, 'ReverseListenerBindAddress': '0.0.0.0', 'PayloadUUIDSeed': '0ba141fe-bd57-11ec-b10f-000c29b3f831', 'ReverseListenerBindPort': None, 'ReverseAllowProxy': False, 'ReverseListenerComm': None, 'ReverseListenerThreaded': False, 'StagerRetryCount': 10, 'StagerRetryWait': 5, 'PingbackRetries': 0, 'PingbackSleep': 30, 'PayloadUUIDRaw': None, 'PayloadUUIDName': None, 'PayloadUUIDTracking': False, 'EnableStageEncoding': False, 'StageEncoder': None, 'StageEncoderSaveRegisters': '', 'StageEncodingFallback': True, 'PrependMigrate': False, 'PrependMigrateProc': None, 'EXITFUNC': 'process', 'AutoLoadStdapi': True, 'AutoVerifySessionTimeout': 30, 'InitialAutoRunScript': '', 'AutoRunScript': '', 'AutoSystemInfo': True, 'EnableUnicodeEncoding': False, 'HandlerSSLCert': None, 'SessionRetryTotal': 31536000, 'SessionRetryWait': 10, 'SessionExpirationTimeout': 94608000, 'SessionCommunicationTimeout': 31536000, 'PayloadProcessCommandLine': '', 'AutoUnhookProcess': False, 'MeterpreterDebugBuild': False, 'TARGET': 0, 'ID': 0, 'Format': 'exe'}}
    #     mname = data.get("mname")
    #     opts = data.get("opts")
    #     if isinstance(opts, str):
    #         opts = json.loads(opts)
    #     response = Payload.create(mname, opts)
    #     return response

    def create(self, request, *args, **kwargs):
        logger.info("前端传递数据为: {}".format(request.data))
        mname = request.data.get("mname")
        opts = request.data.get("opts")
        if isinstance(opts, str):
            opts = json.loads(opts)
        response = Payload.create(mname, opts)
        # return Response(data=byteresult, content_type='application/octet-stream', status=status.HTTP_200_OK)
        return response


class PostModuleActuatorView(BaseView):
    def list(self, request, *args, **kwargs):
        """
        获取模块配置
        """
        context = Xcache.list_moduleconfigs()
        return Response(data=context, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        logger.info("前端传递参数为: {}".format(request.data))
        sessionid = int(request.data.get('sessionid'))
        ipaddress = request.data.get('ipaddress')
        loadpath = request.data.get('loadpath')
        custom_param = request.data.get('custom_param')
        context = PostModuleActuator.create_post(loadpath=loadpath,
                                                 sessionid=sessionid,
                                                 ipaddress=ipaddress,
                                                 custom_param=custom_param)

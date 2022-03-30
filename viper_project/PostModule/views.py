# Create your views here.
from rest_framework.response import Response

from Lib.api import data_return
from Lib.baseview import BaseView
from Lib.configs import CODE_MSG_ZH, CODE_MSG_EN
from Lib.log import logger
from PostModule.Handle.postmoduleactuator import PostModuleActuator
from PostModule.Handle.postmoduleauto import PostModuleAuto
from PostModule.Handle.postmoduleconfig import PostModuleConfig
from PostModule.Handle.postmoduleresult import PostModuleResult
from PostModule.Handle.postmoduleresulthistory import PostModuleResultHistory
from PostModule.Handle.proxyhttpscan import ProxyHttpScan


class PostModuleConfigView(BaseView):
    def list(self, request, **kwargs):
        loadpath = request.query_params.get('loadpath')

        context = PostModuleConfig.list(loadpath=loadpath)
        return Response(context)

    def update(self, request, **kwargs):
        context = PostModuleConfig.update()
        return Response(context)


class PostModuleActuatorView(BaseView):
    def create(self, request, **kwargs):
        # {'ipaddress': '172.16.12.131', 'sessionid': 11, 'loadpath': 'MODULES.DefenseEvasion_ProcessInjection_ProcessHandle', 'custom_param': '{"_msgrpc_handler":"{\\"PAYLOAD\\": \\"windows/x64/meterpreter/reverse_tcp\\", \\"WORKSPACE\\": null, \\"VERBOSE\\": false, \\"WfsDelay\\": 2, \\"EnableContextEncoding\\": false, \\"ContextInformationFile\\": null, \\"DisablePayloadHandler\\": false, \\"ExitOnSession\\": false, \\"ListenerTimeout\\": 0, \\"LHOST\\": \\"172.16.12.135\\", \\"LPORT\\": 1234, \\"ReverseListenerBindAddress\\": \\"0.0.0.0\\", \\"PayloadUUIDSeed\\": \\"118cb5a5-ae7b-11ec-86c4-000c29c3ea5e\\", \\"ReverseListenerBindPort\\": null, \\"ReverseAllowProxy\\": false, \\"ReverseListenerComm\\": null, \\"ReverseListenerThreaded\\": false, \\"StagerRetryCount\\": 10, \\"StagerRetryWait\\": 5, \\"PingbackRetries\\": 0, \\"PingbackSleep\\": 30, \\"PayloadUUIDRaw\\": null, \\"PayloadUUIDName\\": null, \\"PayloadUUIDTracking\\": false, \\"EnableStageEncoding\\": false, \\"StageEncoder\\": null, \\"StageEncoderSaveRegisters\\": \\"\\", \\"StageEncodingFallback\\": true, \\"PrependMigrate\\": false, \\"PrependMigrateProc\\": null, \\"EXITFUNC\\": \\"process\\", \\"AutoLoadStdapi\\": true, \\"AutoVerifySessionTimeout\\": 30, \\"InitialAutoRunScript\\": \\"\\", \\"AutoRunScript\\": \\"\\", \\"AutoSystemInfo\\": true, \\"EnableUnicodeEncoding\\": false, \\"HandlerSSLCert\\": null, \\"SessionRetryTotal\\": 31536000, \\"SessionRetryWait\\": 10, \\"SessionExpirationTimeout\\": 94608000, \\"SessionCommunicationTimeout\\": 31536000, \\"PayloadProcessCommandLine\\": \\"\\", \\"AutoUnhookProcess\\": false, \\"TARGET\\": 0, \\"ID\\": 4}","PID":1884,"ACTION":"inject"}'}
        # logger.info("进程注入前端数据为: {}".format(request.data))
        moduletype = request.data.get('moduletype')
        if moduletype is None:  # 默认模块
            try:
                sessionid = int(request.data.get('sessionid'))
                ipaddress = request.data.get('ipaddress')
                # MODULES.DefenseEvasion_ProcessInjection_ProcessHandle
                loadpath = request.data.get('loadpath')
                custom_param = request.data.get('custom_param')
                context = PostModuleActuator.create_post(loadpath=loadpath,
                                                         sessionid=sessionid,
                                                         ipaddress=ipaddress,
                                                         custom_param=custom_param)
            except Exception as E:
                logger.error(E)
                context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
            return Response(context)
        elif moduletype == "Bot":
            try:
                ipportlist = request.data.get('ipportlist')
                loadpath = request.data.get('loadpath')
                custom_param = request.data.get('custom_param')
                context = PostModuleActuator.create_bot(ipportlist=ipportlist,
                                                        loadpath=loadpath,
                                                        custom_param=custom_param)
            except Exception as E:
                logger.error(E)
                context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
            return Response(context)
        else:
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
            return Response(context)


class PostModuleResultView(BaseView):
    def list(self, request, **kwargs):
        try:
            ipaddress = request.query_params.get('ipaddress')
            loadpath = request.query_params.get('loadpath')
            context = PostModuleResult.list(ipaddress=ipaddress, loadpath=loadpath)
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)


class PostModuleResultHistoryView(BaseView):
    def destroy(self, request, *args, **kwargs):
        try:

            context = PostModuleResultHistory.destory()
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)


class PostModuleAutoView(BaseView):
    def list(self, request, **kwargs):
        try:
            context = PostModuleAuto.list()
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)

    def create(self, request, **kwargs):
        try:
            loadpath = request.data.get('loadpath')
            custom_param = request.data.get('custom_param')
            context = PostModuleAuto.create(loadpath=loadpath,
                                            custom_param=custom_param)
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)

    def destroy(self, request, pk=None, **kwargs):
        try:
            module_uuid = request.query_params.get('_module_uuid')
            context = PostModuleAuto.destory(module_uuid=module_uuid)
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)


class ProxyHttpScanView(BaseView):
    def list(self, request, **kwargs):
        try:
            context = ProxyHttpScan.list()
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)

    def create(self, request, **kwargs):
        try:
            loadpath = request.data.get('loadpath')
            custom_param = request.data.get('custom_param')
            context = ProxyHttpScan.create(loadpath=loadpath,
                                           custom_param=custom_param)
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)

    def destroy(self, request, pk=None, **kwargs):
        try:
            module_uuid = request.query_params.get('_module_uuid')
            context = ProxyHttpScan.destory(module_uuid=module_uuid)
        except Exception as E:
            logger.error(E)
            context = data_return(500, {}, CODE_MSG_ZH.get(500), CODE_MSG_EN.get(500))
        return Response(context)

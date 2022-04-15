from config.viper_config import RPC_SESSION_OPER_SHORT_REQ
from utils.log import logger
from utils.rpcclient import RpcClient
from utils.method import Method


class MSFModule(object):
    def __init__(self):
        pass

    @staticmethod
    def run_msf_module_realtime(module_type=None, mname=None, opts=None, runasjob=False, timeout=RPC_SESSION_OPER_SHORT_REQ):
        params = [
            module_type,
            mname,
            opts,
            runasjob,
            timeout
        ]
        logger.info("发送给MSF的参数为: {}".format(params))
        result = RpcClient.call(Method.ModuleExecute, params, timeout=timeout)
        return result
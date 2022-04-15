from utils.rpcclient import RpcClient
from utils.method import Method
from config.viper_config import RPC_SESSION_OPER_SHORT_REQ


class PortFwd(object):
    @staticmethod
    def list_portfwd():
        result_list = RpcClient.call(Method.SessionMeterpreterPortFwdList, timeout=RPC_SESSION_OPER_SHORT_REQ)
        if result_list is None:
            return []
        else:
            return result_list

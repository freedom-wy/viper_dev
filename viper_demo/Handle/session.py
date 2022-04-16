from utils.rpcclient import RpcClient
from utils.method import Method
from config.viper_config import RPC_FRAMEWORK_API_REQ
from utils.log import logger


class Session(object):
    def __init__(self):
        pass

    @staticmethod
    def list():
        sessions = Session.list_sessions()
        logger.info("session信息为: {}".format(sessions))
        return sessions

    @staticmethod
    def list_sessions():
        """
        远程调用RPC查看session信息
        """
        result = RpcClient.call(Method.SessionList, timeout=RPC_FRAMEWORK_API_REQ)
        if result is None:
            return []
        return result
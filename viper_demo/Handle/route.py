from utils.rcpclient import RpcClient
from utils.method import Method


class Route(object):
    def __init__(self):
        pass

    @staticmethod
    def list_route():
        # 远程调用msfrpc
        result = RpcClient.call(Method.SessionMeterpreterRouteList)
        if result is None:
            return []
        return result

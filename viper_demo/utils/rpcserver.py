from .redisclient import RedisClient
from utils.log import logger
import json


class RPCServer(object):
    def __init__(self):
        self.redis_server = RedisClient.get_result_connection()
        self.message_queue = "rpcviper"

    def run(self):
        while True:
            message_queue, message = self.redis_server.blpop(self.message_queue)
            logger.info("message_queue: {}, message: {}".format(message_queue, message.decode()))
            message_queue = message_queue.decode()
            if message_queue != self.message_queue:
                logger.warning(f"message_queue 错误: {message_queue} {self.message_queue}")
                continue
            # try:
            rpc_request = json.loads(message.decode())
            #     function_call = rpc_request.get('function_call')
            response_queue = rpc_request.get('response_queue')
            #     function = function_call.get("function")
            #     kwargs = function_call.get("kwargs")
            # except Exception as E:
            #     logger.warning("请求解析失败")
            #     logger.exception(E)
            #     continue
            rpc_response = True
            # 向msf发送数据
            self.redis_server.rpush(response_queue, json.dumps(rpc_response))


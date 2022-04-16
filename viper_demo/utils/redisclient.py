import redis
from utils.log import logger
from config.viper_config import REDIS_HOST, REDIS_PORT
from config.secure_config import RPC_TOKEN


class RedisClient(object):
    def __init__(self):
        pass

    @staticmethod
    def get_result_connection():
        try:
            # rcon = redis.Redis.from_url(url=f"{REDIS_URL}5")
            pool = redis.ConnectionPool.from_url(url="redis://:{}@{}:{}/5".format(RPC_TOKEN, REDIS_HOST, REDIS_PORT))
            rcon = redis.StrictRedis(connection_pool=pool)
            return rcon
        except Exception as E:
            logger.warning(E)
            return None

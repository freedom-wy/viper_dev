import redis
from utils.log import logger
from config.viper_config import REDIS_URL


class RedisClient(object):
    def __init__(self):
        pass

    @staticmethod
    def get_result_connection():
        try:
            rcon = redis.Redis.from_url(url=f"{REDIS_URL}5")
            return rcon
        except Exception as E:
            logger.warning(E)
            return None

import time
from utils.rpcclient import RpcClient
from utils.method import Method
from config.viper_config import RPC_FRAMEWORK_API_REQ
from utils.log import logger


class Job(object):
    def __init__(self):
        pass

    @staticmethod
    def is_msf_job_alive(job_id):
        """
        查看MSF中是否存在该ID
        """
        time.sleep(0.5)
        try:
            result = RpcClient.call(Method.JobList, timeout=RPC_FRAMEWORK_API_REQ)
            # Xcache.set_msf_job_cache(result)
            if result is None:
                return False
            else:
                if result.get(str(job_id)) is not None:
                    return True
                else:
                    return False
        except Exception as E:
            logger.error(E)
            return False
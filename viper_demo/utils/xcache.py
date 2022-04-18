from utils.log import logger
from django.core.cache import cache
import time


class Xcache(object):
    """
    缓存模块
    """
    XCACHE_MODULES_CONFIG = "XCACHE_MODULES_CONFIG"
    XCACHE_MODULES_TASK_LIST = "XCACHE_MODULES_TASK_LIST"

    def __init__(self):
        pass

    @staticmethod
    def get_moduleconfig(loadpath):
        modules_config = cache.get(Xcache.XCACHE_MODULES_CONFIG)
        try:
            for config in modules_config:
                if config.get("loadpath") == loadpath:
                    return config
            return None
        except Exception as E:
            logger.error(E)
            return None

    @staticmethod
    def update_moduleconfigs(all_modules_config):
        cache.set(Xcache.XCACHE_MODULES_CONFIG, all_modules_config, None)
        return True

    @staticmethod
    def list_moduleconfigs():
        modules_config = cache.get(Xcache.XCACHE_MODULES_CONFIG)
        if not modules_config:
            return []
        return modules_config

    @staticmethod
    def init_xcache_on_start():
        # 清理模块配置缓存
        cache.set(Xcache.XCACHE_MODULES_CONFIG, None, None)
        return True

    @staticmethod
    def get_module_task_by_uuid_nowait(task_uuid):
        key = "{}_{}".format(Xcache.XCACHE_MODULES_TASK_LIST, task_uuid)
        req = cache.get(key)
        return req

    @staticmethod
    def create_module_task(req):
        for i in range(5):
            key = f"{Xcache.XCACHE_MODULES_TASK_LIST}_{req.get('uuid')}"
            cache.set(key, req, None)
            if cache.get(key) is not None:
                break
            else:
                logger.error("redis 缓存失败!")
            time.sleep(0.5)
        return True

    @staticmethod
    def del_module_task_by_uuid(task_uuid):
        key = "{}_{}".format(Xcache.XCACHE_MODULES_TASK_LIST, task_uuid)
        cache.delete(key)



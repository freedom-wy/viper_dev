import importlib
from config.viper_config import BROKER
from utils.xcache import Xcache
import json
from utils.apsmodule import aps_module


class PostModuleActuator(object):
    def __init__(self):
        pass

    @staticmethod
    def create_post(loadpath=None, sessionid=None, ipaddress=None, custom_param=None):
        # 获取模块配置
        # module_config = Xcache.get_moduleconfig(loadpath)
        custom_param = json.loads(custom_param)
        # 获取模块实例
        class_inntent = importlib.import_module(loadpath)
        # 向模块传参
        post_module_intent = class_inntent.PostModule(sessionid, ipaddress, custom_param)
        # 模块执行环境检查
        # check_result = post_module_intent.check()
        broker = post_module_intent.MODULE_BROKER
        if broker == BROKER.post_python_job:
            # 放入队列
            aps_module.putin_post_python_module_queue(post_module_intent)
            return post_module_intent.NAME_ZH












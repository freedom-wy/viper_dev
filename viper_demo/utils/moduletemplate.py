from config.viper_config import BROKER
from config.viper_config import TAG2TYPE
import threading
from utils.xcache import Xcache
import time


class _CommonModule(object):
    MODULE_BROKER = BROKER.empty

    NAME_ZH = "基础模块"
    DESC_ZH = "基础描述"
    NAME_EN = "基础模块名称英文"
    DESC_EN = "基础模块名称英文"
    WARN_ZH = None
    WARN_EN = None

    AUTHOR = ["王胖胖"]
    REFERENCES = []
    README = []

    MODULETYPE = TAG2TYPE.example
    OPTIONS = []

    # post类模块描述
    REQUIRE_SESSION = False  # 模块是否需要session
    PLATFORM = ["Windows", "Linux"]  # 平台
    PERMISSIONS = ["User", "Administrator", "SYSTEM", "Root"]  # 所需权限
    ATTCK = []

    def __init__(self, custom_param):
        super().__init__()
        self._custom_param = custom_param  # 前端传入的信息
        # self._ipaddress = None
        # self._sessionid = None
        self._ip = None
        self._port = None
        self._protocol = None
        self._module_uuid = None
        self.opts = {}

    def check(self):
        return True, None


class _PostCommonModule(_CommonModule):
    def __init__(self, sessionid, ipaddress, custom_param):
        super().__init__(custom_param)
        # 前端传入的IP地址和SESSIONID
        self._ipaddress = ipaddress
        self._sessionid = sessionid


class PostPythonModule(_PostCommonModule):
    MODULE_BROKER = BROKER.post_python_job

    def __init__(self, sessionid, ipaddress, custom_param):
        super().__init__(sessionid, ipaddress, custom_param)
        # 模块是否退出
        self.exit_flag = False

    def _thread_run(self):
        t1 = threading.Thread(target=self.run)
        t1.start()

        while True:
            # 可能手动删除
            req = Xcache.get_module_task_by_uuid_nowait(self._module_uuid)
            # 模块已执行完成
            if not req:
                break
            elif not t1.is_alive():
                break
            else:
                time.sleep(1)

    def run(self):
        """
        具体模块执行的逻辑
        """
        pass

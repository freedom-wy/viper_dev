from config.viper_config import BROKER
from config.viper_config import TAG2TYPE
import threading
from utils.xcache import Xcache
import time
import json
from utils.log import logger
from config.viper_config import HANDLER_OPTION, CREDENTIAL_OPTION, FILE_OPTION
from Handle.payload import Payload
import os
from config.viper_config import MODULE_DATA_DIR
from jinja2 import Environment, FileSystemLoader
import random
import string


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

    def param(self, name):
        if name in [HANDLER_OPTION.get('name'), CREDENTIAL_OPTION.get('name'), FILE_OPTION.get('name')]:
            if self._custom_param.get(name) is None:
                return None
            try:
                tmp_param = json.loads(self._custom_param.get(name))
                return tmp_param
            except Exception as E:
                logger.warning(E)
                return None

        else:
            return self._custom_param.get(name)

    @property
    def loadpath(self):
        """获取模块加载路径"""
        return self.__module__

    @property
    def module_data_dir(self):
        """模块对应的Data目录路径"""
        return os.path.join(MODULE_DATA_DIR, self.loadpath.split(".")[-1])

    def generate_context_by_template(self, filename, **kwargs):
        """根据模板获取内容"""
        env = Environment(loader=FileSystemLoader(self.module_data_dir))
        tpl = env.get_template(filename)
        context = tpl.render(**kwargs)
        return context

    @staticmethod
    def random_str(num):
        """生成随机字符串"""
        salt = ''.join(random.sample(string.ascii_letters, num))
        return salt


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

    def generate_hex_reverse_shellcode_by_handler(self):
        """
        生成shellcode
        """
        # 获取前端传递过来的参数
        handle_config = self.param(HANDLER_OPTION.get("name"))
        if not handle_config:
            return None
        shellcode = Payload.generate_shellcode(mname=handle_config.get("PAYLOAD"), opts=handle_config)
        logger.info("shellcode的类型为: {}".format(type(shellcode)))
        reverse_hex_str = shellcode.hex()[::-1]
        return reverse_hex_str


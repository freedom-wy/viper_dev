from utils.moduletemplate import PostPythonModule
from config.viper_config import TAG2TYPE
from utils.option import OptionHandler, OptionStr, register_options
from utils.log import logger
import time


class PostModule(PostPythonModule):
    NAME_ZH = "伪造成word文档的exe文件"
    DESC_ZH = "带有word图标的exe文件, exe运行后自动释放内置的word文档, 自动拷贝到Document目录下并启动自身，然后删除自身"
    MODULETYPE = TAG2TYPE.Initial_Access
    PLATFORM = ["Windows"]
    PERMISSIONS = ["User", "Administrator", "SYSTEM"]
    ATTACK = []
    README = ["http://测试"]
    REFERENCES = ["http://测试"]
    AUTHOR = ["王胖胖"]

    # 校验前端传递参数
    OPTIONS = register_options(
        [
            OptionHandler(),
            OptionStr(
                name='LoaderName',
                tag_zh="进程名称", desc_zh="载荷的进程名称,建议仿冒系统进程名,增强迷惑性.",
                tag_en="Process name",
                desc_en="Process name of the payload.It is recommended to fake the name of the system process to enhance the confusion.",
                default="dllhost.exe"
            )
        ]
    )

    def __init__(self, sessionid, ipaddress, custom_param):
        super().__init__(sessionid, ipaddress, custom_param)

    def check(self):
        return True, None

    def run(self):
        time.sleep(10)
        logger.info("执行具体模块")





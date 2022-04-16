# 监控
from apscheduler.schedulers.background import BackgroundScheduler
from .rpcserver import RPCServer
from utils.log import logger
import logging


class MainMonitor(object):
    def __init__(self):
        pass

    def start(self):
        # 创建一个后台运行的监控线程
        # 关闭apscheduler的警告
        log = logging.getLogger('apscheduler.scheduler')
        log.setLevel(logging.ERROR)
        self.MainScheduler = BackgroundScheduler()

        self.MainScheduler.add_job(
            func=MainMonitor.sub_msf_rpc_thread,
            max_instances=1,
            trigger="interval",
            seconds=1,
            id="sub_msf_rpc_thread"
        )
        self.MainScheduler.start()

    @staticmethod
    def sub_msf_rpc_thread():
        logger.info("监控msf发来的消息")
        RPCServer().run()




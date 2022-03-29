from django.conf.urls import url, include
from rest_framework import routers

from Core.views import BaseAuthView, CurrentUserView, NoticesView, SettingView, HostView, HostInfoView, UUIDJsonView
from Core.views import NetworkSearchView
from Lib.montior import MainMonitor
from Msgrpc.views import LazyLoaderView, LazyLoaderInterfaceView, CollectSandBoxInterfaceView, CollectSandBoxView
from Msgrpc.views import ServiceStatusView, PayloadView, JobView, HandlerView, SessionView, SessionIOView, RouteView
from Msgrpc.views import SocksView, TransportView, FileMsfView, FileSessionView, PortFwdView, HostFileView
from Msgrpc.views import WebDeliveryView, IPFilterView
from PostLateral.views import PortServiceView, CredentialView, VulnerabilityView
from PostModule.views import PostModuleConfigView, PostModuleActuatorView, PostModuleResultView, ProxyHttpScanView
from PostModule.views import PostModuleResultHistoryView, PostModuleAutoView

router = routers.DefaultRouter()
# 登录认证
router.register(r'api/v1/core/baseauth', BaseAuthView, basename="BaseAuth")
# 获取当前登录用户信息
router.register(r'api/v1/core/currentuser', CurrentUserView, basename="CurrentUser")
router.register(r'api/v1/core/notices', NoticesView, basename="Notice")
router.register(r'api/v1/core/setting', SettingView, basename="Setting")
router.register(r'api/v1/core/host', HostView, basename="Host")
router.register(r'api/v1/core/hostinfo', HostInfoView, basename="HostInfo")
router.register(r'api/v1/core/uuidjson', UUIDJsonView, basename="UUIDJsonView")

router.register(r'api/v1/core/networksearch', NetworkSearchView, basename="NetworkSearch")
router.register(r'api/v1/msgrpc/servicestatus', ServiceStatusView, basename="ServiceStatus")
# 生成载荷
router.register(r'api/v1/msgrpc/payload', PayloadView, basename="Payload")
router.register(r'api/v1/msgrpc/job', JobView, basename="Job")
# 监听载荷
router.register(r'api/v1/msgrpc/handler', HandlerView, basename="Handler")
router.register(r'api/v1/msgrpc/webdelivery', WebDeliveryView, basename="WebDelivery")
# 获取session详细信息
router.register(r'api/v1/msgrpc/session', SessionView, basename="Session")
router.register(r'api/v1/msgrpc/sessionio', SessionIOView, basename="SessionIO")
router.register(r'api/v1/msgrpc/route', RouteView, basename="Route")
router.register(r'api/v1/msgrpc/socks', SocksView, basename="Socks")
router.register(r'api/v1/msgrpc/portfwd', PortFwdView, basename="PortFwd")
router.register(r'api/v1/msgrpc/transport', TransportView, basename="Transport")
router.register(r'api/v1/msgrpc/filemsf', FileMsfView, basename="FileMsfView")
router.register(r'api/v1/msgrpc/filesession', FileSessionView, basename="FileSessionView")
router.register(r'api/v1/msgrpc/lazyloader', LazyLoaderView, basename="LazyLoaderView")
router.register(r'api/v1/msgrpc/collectsandbox', CollectSandBoxView, basename="CollectSandBoxView")
router.register(r'api/v1/msgrpc/ipfilter', IPFilterView, basename="IPFilterView")

router.register(r'api/v1/postlateral/portservice', PortServiceView, basename="PortServiceView")
router.register(r'api/v1/postlateral/credential', CredentialView, basename="CredentialView")
router.register(r'api/v1/postlateral/vulnerability', VulnerabilityView, basename="VulnerabilityView")
router.register(r'api/v1/postmodule/postmoduleconfig', PostModuleConfigView, basename="PostModuleConfig")
router.register(r'api/v1/postmodule/postmoduleactuator', PostModuleActuatorView, basename="PostModuleActuator")
router.register(r'api/v1/postmodule/postmoduleresult', PostModuleResultView, basename="PostModuleResult")
router.register(r'api/v1/postmodule/postmoduleresulthistory', PostModuleResultHistoryView,
                basename="PostModuleResultHistoryView")
router.register(r'api/v1/postmodule/postmoduleauto', PostModuleAutoView,
                basename="PostModuleAutoView")
router.register(r'api/v1/postmodule/proxyhttpscan', ProxyHttpScanView,
                basename="ProxyHttpScanView")
# 无需认证的api
router.register(r'api/v1/d', HostFileView, basename="HostFileView")
router.register(r'api/v1/c', LazyLoaderInterfaceView, basename="LazyLoaderInterfaceView")
router.register(r'api/v1/a', CollectSandBoxInterfaceView, basename="CollectSandBoxInterfaceView")

urlpatterns = [
    url(r'^', include(router.urls)),
]

# 监控
MainMonitor().start()

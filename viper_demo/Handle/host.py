from apps.demo.models import HostModel
from apps.demo.serializers import HostSerializer
from Handle.route import Route
from Handle.socks import Socks
from Handle.portfwd import PortFwd
from Handle.portservice import PortService
import ipaddress as ipaddr
from utils.log import logger


class Host(object):
    def __init__(self):
        pass

    @staticmethod
    def list():
        # 所有主机数据
        hosts = Host.list_hosts()
        logger.info("主机数据: {}".format(hosts))
        # 所有路由信息
        route_list = Route.list_route()
        logger.info("路由数据: {}".format(route_list))
        # 所有连接信息
        socks_list = Socks.list_msf_socks()
        logger.info("连接信息数据: {}".format(socks_list))
        # 所有端口转发信息
        portfwd_list = PortFwd.list_portfwd()
        logger.info("端口转发数据: {}".format(portfwd_list))

        # 格式化主机数据
        for host in hosts:
            ipaddress = host.get('ipaddress')
            # 端口信息
            host['portService'] = PortService.list_by_ipaddress(ipaddress)
            # 路由信息
            for route in route_list:
                ipnetwork = ipaddr.ip_network(f"{route.get('subnet')}/{route.get('netmask')}", strict=False)
                if ipaddr.ip_address(ipaddress) in ipnetwork:
                    host['route'] = {'type': 'ROUTE', 'data': route.get("session")}
                    break
            else:
                host['route'] = {'type': 'DIRECT', 'data': None}

        result = {'hosts': hosts, 'routes': route_list, 'socks': socks_list, 'portfwds': portfwd_list, }
        return result



    @staticmethod
    def list_hosts():
        """
        序列化HostModels中所有数据
        """
        models = HostModel.objects.all()
        # 序列化
        result = HostSerializer(instance=models, many=True).data
        return result






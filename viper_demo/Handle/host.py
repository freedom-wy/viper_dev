from apps.demo.models import HostModel
from apps.demo.serializers import HostSerializer
from Handle.route import Route


class Host(object):
    def __init__(self):
        pass

    @staticmethod
    def list():
        # 所有主机数据
        hosts = Host.list_hosts()
        # 所有路由信息
        route_list = Route.list_route()
        # 所有连接信息
        # 所有端口转发信息

    @staticmethod
    def list_hosts():
        """
        序列化HostModels中所有数据
        """
        models = HostModel.objects.all()
        # 序列化
        result = HostSerializer(instance=models, many=True)
        return result






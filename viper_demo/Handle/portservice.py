from utils.log import logger
from apps.demo.models import PortServiceModel
from apps.demo.serializers import PortServiceSerializer


class PortService(object):
    def __init__(self):
        pass

    @staticmethod
    def list_by_ipaddress(ipaddress=None):
        models = PortServiceModel.objects.filter(ipaddress=ipaddress).order_by('port')
        data = PortServiceSerializer(models, many=True).data
        try:
            format_data = PortService.format_banner(data)
        except Exception as E:
            format_data = data
            logger.error(E)
        return format_data

    @staticmethod
    def format_banner(port_service_list=None):
        """将服务信息格式化"""
        for port_service in port_service_list:
            output_str = ""
            if port_service.get('banner').get('vendorproductname'):
                output_str += f"Product: {','.join(port_service.get('banner').get('vendorproductname'))}\t"

            if port_service.get('banner').get('version'):
                output_str += f"Version: {','.join(port_service.get('banner').get('version'))}\t"

            if port_service.get('banner').get('info'):
                info = ",".join(port_service.get('banner').get('info'))
                info = info.replace('\x00', '').replace('\0', '')
                output_str += f"Info: {info}\t"

            if port_service.get('banner').get('hostname'):
                hostname = ",".join(port_service.get('banner').get('hostname'))
                hostname = hostname.replace('\x00', '').replace('\0', '')
                output_str += f"Hostname: {hostname}\t"

            if port_service.get('banner').get('operatingsystem'):
                output_str += f"OS: {','.join(port_service.get('banner').get('operatingsystem'))}\t"

            if port_service.get('banner').get('devicetype'):
                output_str += f"Device: {','.join(port_service.get('banner').get('devicetype'))}\t"

            if port_service.get('banner').get('mac'):
                output_str += f"MAC: {port_service.get('banner').get('mac')}\t"

            if port_service.get('banner').get('other'):
                output_str += f"Raw: {port_service.get('banner').get('other')}\t"
            port_service['banner'] = output_str
        return port_service_list

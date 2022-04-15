from django.db import models
from utils.base_models import BaseModels
import ast


# Create your models here.

class HostModel(BaseModels):
    TAG = (
        ('web_server', 'web_server'),  # web服务器
        ('db_server', "db_server"),  # 数据库服务器
        ('firewall', "firewall"),  # 防火墙设备
        ('ad_server', "ad_server"),  # 域控服务器
        ('pc', "pc"),  # 个人pc
        ('oa', "oa"),  # 域控服务器
        ('cms', "cms"),  # 域控服务器
        ('other', "other"),  # 其他
    )

    ipaddress = models.CharField(blank=True, null=True, max_length=100)
    tag = models.CharField(choices=TAG, max_length=50, default="other")
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "viper_host"
        verbose_name = "viper的主机表"
        verbose_name_plural = verbose_name


class DiyDictField(models.TextField):
    """数据库中用来存储dict类型字段"""
    description = "Stores a python dict"

    def __init__(self, *args, **kwargs):
        super(DiyDictField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):  # 将python对象转为查询值
        if value is None:
            return value

        return str(value)  # use str(value) in Python 3

    def from_db_value(self, value, expression, connection):
        if not value:
            value = []
        if isinstance(value, dict):
            return value
        # 直接将字符串转换成python内置的list
        try:
            return ast.literal_eval(value)
        except Exception as E:
            from Lib.log import logger
            logger.exception(E)
            logger.error(value)
            return {}

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class PortServiceModel(models.Model):
    ipaddress = models.CharField(blank=True, null=True, max_length=100)
    update_time = models.IntegerField(default=0)
    port = models.IntegerField(default=0)
    banner = DiyDictField(default={})
    service = models.CharField(blank=True, null=True, max_length=100)



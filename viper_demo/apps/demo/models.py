from django.db import models
from utils.base_models import BaseModels


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



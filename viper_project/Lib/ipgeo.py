# -*- coding: utf-8 -*-
# @File  : ipgeo.py
# @Date  : 2021/11/9
# @Desc  :
from Lib.External.geoip2 import geoip2_instance
from Lib.External.ip2Region import ip2region_instance
from Lib.xcache import Xcache


class IPGeo(object):
    @staticmethod
    def get_ip_geo(ip, lang="zh-CN"):
        # search from cache
        key = f"{ip}-{lang}"
        # 从缓存XCACHE_GEOIP_DATA中获取IP地理位置信息
        geo_list = Xcache.get_geoip_data(key)
        if geo_list is not None:
            return geo_list

        if lang == "zh-CN":
            # 从数据库STATICFILES/STATIC/ip2region.db中获取IP地理位置信息
            geo_list = ip2region_instance.get_geo(ip)
            if geo_list is None:
                geo_list = geoip2_instance.get_geo(ip, lang)
        elif lang == "en-US":
            geo_list = geoip2_instance.get_geo(ip, "en")
        else:
            geo_list = ["", "", "", ""]

        # 将获取到的IP地理位置信息设置到缓存中
        Xcache.set_geoip_data(key, geo_list)
        return geo_list

    @staticmethod
    def get_ip_geo_str(ip, lang="zh-CN"):
        geo_list = IPGeo.get_ip_geo(ip, lang)
        return " ".join(geo_list)

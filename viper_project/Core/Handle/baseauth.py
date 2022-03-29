# -*- coding: utf-8 -*-
# @File  : baseauth.py
# @Date  : 2021/2/25
# @Desc  :
import datetime

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from Lib.configs import EXPIRE_MINUTES
from Lib.xcache import Xcache
from Lib.log import logger


# 自定义认证方法
class BaseAuth(TokenAuthentication):
    def authenticate_credentials(self, key=None):
        # logger.info("传递过来的token为: {}".format(key))
        # 搜索缓存的user token
        cache_user = Xcache.alive_token(key)
        # logger.info("用户信息为: {}".format(cache_user))
        if cache_user:
            return cache_user, key

        # 数据库中校验token
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed()

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed()

        # token超时清理
        time_now = datetime.datetime.now()
        if token.created < time_now - datetime.timedelta(minutes=EXPIRE_MINUTES):
            token.delete()
            raise exceptions.AuthenticationFailed()

        # 缓存token
        if token:
            logger.info("向redis保存用户token信息")
            Xcache.set_token_user(key, token.user)
        return token.user, token

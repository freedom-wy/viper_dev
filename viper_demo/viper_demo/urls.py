"""viper_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from apps.demo.views import HostView, HandleView, PayloadView, SessionView, PostModuleActuatorView
from rest_framework import routers
from django.urls import path, include, re_path
from utils.montior import MainMonitor


router = routers.DefaultRouter()
router.register(r'api/v1/core/host', HostView, basename="Host")
router.register(r'api/v1/core/session', SessionView, basename="Session")
router.register(r'api/v1/msgrpc/handler', HandleView, basename="Handler")
router.register(r'api/v1/msgrpc/payload', PayloadView, basename="Payload")
router.register(r'api/v1/postmodule/postmoduleactuator', PostModuleActuatorView, basename="PostModuleActuator")



urlpatterns = [
    re_path("^", include(router.urls)),
    path('admin/', admin.site.urls),
]

# 调用监控
MainMonitor().start()

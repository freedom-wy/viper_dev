from django.db import models
from django.utils.timezone import now


class BaseModels(models.Model):
    add_time = models.DateTimeField(default=now, verbose_name="添加时间")

    class Meta:
        abstract = True



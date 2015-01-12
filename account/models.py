# coding: UTF-8
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, verbose_name='用户')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.user.username
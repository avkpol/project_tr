# -*- coding: utf-8 -*-
from django.db import models


class Control(models.Model):
    '''Control Model'''
    class Meta(object):
        verbose_name= u"Control"

    parent_id = models.IntegerField(
        blank = False,
        default = 0,
        verbose_name = u"Parent ID")
    name = models.CharField(
        max_length = 256,
        blank = False,
        verbose_name= u"Name")
    url=models.CharField(
        max_length = 256,
        blank=False,
        verbose_name = u"URL")
    # noinspection PyUnresolvedReferences
    # type = models.OneToOneField('ControlType',
    type = models.CharField(
        max_length = 256,
        verbose_name=u"Type",
        blank=False,
        null=True)
        # on_delete=models.PROTECT)    # original:     on_delete=models.PROTECT)
    # noinspection PyUnresolvedReferences
    # control_type = models.OneToOneField('ControlClassification',
    control_type = models.CharField(
        max_length = 256,
        verbose_name=u"Classification",
        blank=False,
        null=True)
        # on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s" % self.name

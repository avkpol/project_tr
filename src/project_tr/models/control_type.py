# -*- coding: utf-8 -*-
from django.db import models


class ControlType(models.Model):
    '''Control Model'''
    class Meta(object):
        verbose_name= u"ControlType"

    # noinspection PyUnresolvedReferences
    name = models.CharField(
        max_length = 256,
        blank=False,
        verbose_name= u"Name")
        # on_delete=models.PROTECT)


    def __unicode__(self):
        return u"%s" % (self.name )

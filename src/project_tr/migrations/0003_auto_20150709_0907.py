# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_tr', '0002_auto_20150709_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='control_type',
            field=models.CharField(max_length=256, null=True, verbose_name='Classification'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='type',
            field=models.CharField(max_length=256, null=True, verbose_name='Type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='controlclassification',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='controltype',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
            preserve_default=True,
        ),
    ]

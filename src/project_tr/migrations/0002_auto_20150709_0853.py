# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_tr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='control_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, \
                                       verbose_name='Classification', to='project_tr.ControlClassification'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, \
                                       verbose_name='Type', to='project_tr.ControlType'),
            preserve_default=True,
        ),
    ]

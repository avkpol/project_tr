# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_id', models.IntegerField(default=0, verbose_name='Parent ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('url', models.CharField(max_length=256, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Control',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControlClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Name', to='project_tr.Control')),
            ],
            options={
                'verbose_name': 'ControlClassification',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControlType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Name', to='project_tr.Control')),
            ],
            options={
                'verbose_name': 'ControlType',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='control',
            name='control_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Classification', to='project_tr.ControlType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='control',
            name='type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, verbose_name='Type', to='project_tr.ControlClassification'),
            preserve_default=True,
        ),
    ]

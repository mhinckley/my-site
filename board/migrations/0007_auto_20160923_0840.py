# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20160923_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='support_link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='when',
            field=models.CharField(max_length=50),
        ),
    ]

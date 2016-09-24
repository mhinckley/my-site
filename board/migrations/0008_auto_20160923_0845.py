# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20160923_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contributor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(max_length=400),
        ),
    ]

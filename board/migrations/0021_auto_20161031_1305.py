# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0020_auto_20161031_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='post',
            name='support_link',
        ),
        migrations.RemoveField(
            model_name='post',
            name='when',
        ),
    ]

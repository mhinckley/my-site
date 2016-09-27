# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='all_follows',
        ),
        migrations.RemoveField(
            model_name='post',
            name='daily_follows',
        ),
        migrations.RemoveField(
            model_name='post',
            name='monthly_follows',
        ),
        migrations.RemoveField(
            model_name='post',
            name='weekly_follows',
        ),
        migrations.AlterField(
            model_name='follow',
            name='frequency',
            field=models.PositiveSmallIntegerField(choices=[(1, b'daily'), (3, b'weekly'), (6, b'monthly')]),
        ),
    ]

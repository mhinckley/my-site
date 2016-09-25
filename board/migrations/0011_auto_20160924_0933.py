# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0010_post_daily_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='monthly_follows',
            field=models.ManyToManyField(related_name='monthly_follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='weekly_follows',
            field=models.ManyToManyField(related_name='weekly_follows', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0009_remove_post_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='daily_follows',
            field=models.ManyToManyField(related_name='daily_follows', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20160923_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content_type',
        ),
    ]

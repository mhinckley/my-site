# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20160925_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='post',
        ),
        migrations.DeleteModel(
            name='HashTag',
        ),
    ]

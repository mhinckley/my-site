# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='tweet',
            new_name='post',
        ),
    ]

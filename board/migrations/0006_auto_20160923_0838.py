# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='do_field',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='post',
            name='to_field',
            field=models.CharField(max_length=50),
        ),
    ]

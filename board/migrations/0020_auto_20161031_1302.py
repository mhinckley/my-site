# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_auto_20160927_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='entry',
            field=models.CharField(max_length=100),
        ),
    ]

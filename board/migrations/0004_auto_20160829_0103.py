# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_post_contributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(default=b'Science', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='contributor',
            field=models.CharField(default=b'Smart person', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(default=b'This is a summary.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='support_link',
            field=models.CharField(default=b'www.expert.edu', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='when',
            field=models.CharField(default=b'All day', max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_auto_20160927_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.ForeignKey(to='board.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(to='board.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='posttag',
            unique_together=set([('post', 'tag')]),
        ),
    ]

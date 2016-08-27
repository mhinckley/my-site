# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_field', models.CharField(default=b'xxx', max_length=50)),
                ('do_field', models.CharField(default=b'xxx', max_length=75)),
                ('when', models.CharField(default=b'sss', max_length=50)),
                ('content_type', models.CharField(default=b'some string', max_length=50, blank=True)),
                ('support_link', models.CharField(default=b'xxx', max_length=1000)),
                ('summary', models.TextField(default=b'xxx', max_length=1000)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=datetime.datetime(2015, 11, 23, 7, 38, 39, 778158, tzinfo=utc), max_length=10000, verbose_name='\u5185\u5bb9'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20151123_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570'),
        ),
    ]

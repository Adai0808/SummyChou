# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='articles_count',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6587\u7ae0\u6570\u91cf'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='browse',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u6570'),
        ),
    ]

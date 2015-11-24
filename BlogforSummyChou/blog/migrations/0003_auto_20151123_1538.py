# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_block_articles_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': '\u7248\u5757', 'verbose_name_plural': '\u7248\u5757'},
        ),
    ]

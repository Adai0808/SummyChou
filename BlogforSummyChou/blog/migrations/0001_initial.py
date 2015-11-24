# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u7248\u5757\u540d\u79f0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(verbose_name='\u7ba1\u7406\u5458', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7248\u5757\u540d\u79f0',
                'verbose_name_plural': '\u7248\u5757\u540d\u79f0',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('brief', models.CharField(max_length=1000, verbose_name='\u7b80\u4ecb')),
                ('tag', models.CharField(max_length=200, verbose_name='\u6982\u8981')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('label', models.ForeignKey(verbose_name='\u6807\u7b7e', to='blog.Block')),
                ('owner', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u6807\u9898',
                'verbose_name_plural': '\u6587\u7ae0\u6807\u9898',
            },
        ),
    ]

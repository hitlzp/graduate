# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='biaoti')),
                ('content', models.TextField(verbose_name='neirong')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='fabiaoshijian')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='gengxinshijian', null=True)),
            ],
        ),
    ]

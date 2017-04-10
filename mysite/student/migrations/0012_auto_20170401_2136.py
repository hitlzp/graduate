# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20170401_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='segmnet_t',
            name='isvalid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='table_t',
            name='choice',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_remove_table_t_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_t',
            name='ratio',
            field=models.IntegerField(default=0),
        ),
    ]

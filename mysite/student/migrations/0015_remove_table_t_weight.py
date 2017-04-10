# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_table_t_ratio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_t',
            name='weight',
        ),
    ]

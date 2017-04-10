# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20170401_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_t',
            name='table',
        ),
    ]

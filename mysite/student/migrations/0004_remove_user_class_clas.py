# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20170327_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_class',
            name='clas',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20170414_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='pingjia',
        ),
    ]

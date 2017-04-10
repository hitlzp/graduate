# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20170401_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_t',
            name='starttime',
            field=models.DateTimeField(default=b'2017-01-01 00:00:00'),
        ),
    ]

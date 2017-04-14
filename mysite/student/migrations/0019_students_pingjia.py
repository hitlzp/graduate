# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20170408_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='pingjia',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]

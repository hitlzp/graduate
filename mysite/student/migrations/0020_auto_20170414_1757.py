# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_students_pingjia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='pingjia',
            field=models.CharField(max_length=100),
        ),
    ]

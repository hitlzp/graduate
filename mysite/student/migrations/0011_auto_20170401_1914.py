# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_course_t_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_t',
            name='recommend',
            field=models.CharField(max_length=1000),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_course_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_t',
            name='sum',
            field=models.IntegerField(default=0),
        ),
    ]

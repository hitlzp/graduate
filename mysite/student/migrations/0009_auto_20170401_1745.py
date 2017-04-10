# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20170331_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segmnet_t',
            old_name='tablesum',
            new_name='ratio',
        ),
        migrations.AddField(
            model_name='course_t',
            name='isvalid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course_t',
            name='mytype',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='table_t',
            name='table',
            field=models.IntegerField(default=0),
        ),
    ]

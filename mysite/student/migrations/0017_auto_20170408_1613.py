# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20170408_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stucourse',
            old_name='student',
            new_name='stu',
        ),
    ]

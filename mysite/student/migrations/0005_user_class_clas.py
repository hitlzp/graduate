# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_user_class_clas'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_class',
            name='clas',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe7\xb1\xbb\xe5\x88\xab'),
        ),
    ]

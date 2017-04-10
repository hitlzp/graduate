# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_auto_20170324_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clas', models.IntegerField(verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe7\xb1\xbb\xe5\x88\xab')),
                ('person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]

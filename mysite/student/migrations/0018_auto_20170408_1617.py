# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0017_auto_20170408_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.IntegerField(default=0)),
                ('grade', models.FloatField(default=0)),
                ('course', models.ForeignKey(to='student.Course_t')),
                ('stu', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='stucourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='stucourse',
            name='stu',
        ),
        migrations.DeleteModel(
            name='Stucourse',
        ),
    ]

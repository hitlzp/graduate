# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0015_remove_table_t_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stucourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.IntegerField(default=0)),
                ('grade', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='course_t',
            name='recommend',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='segmnet_t',
            name='content',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='stucourse',
            name='course',
            field=models.ForeignKey(to='student.Course_t'),
        ),
        migrations.AddField(
            model_name='stucourse',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

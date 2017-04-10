# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_course_t_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segmnet_t',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sname', models.CharField(max_length=100, verbose_name=b'\xe7\x8e\xaf\xe8\x8a\x82\xe5\x90\x8d\xe7\xa7\xb0')),
                ('minute', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=1000)),
                ('tablesum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Table_t',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0)),
                ('tsegment', models.ForeignKey(to='student.Segmnet_t')),
            ],
        ),
        migrations.AddField(
            model_name='course_t',
            name='groupsum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course_t',
            name='recommend',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course_t',
            name='segmentsum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='segmnet_t',
            name='tcourse',
            field=models.ForeignKey(to='student.Course_t'),
        ),
    ]

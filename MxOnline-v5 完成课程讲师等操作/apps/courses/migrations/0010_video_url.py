# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-02 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-11-13 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20171102_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6e\u64ad'),
        ),
    ]
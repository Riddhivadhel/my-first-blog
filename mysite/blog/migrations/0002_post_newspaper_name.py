# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='newspaper_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

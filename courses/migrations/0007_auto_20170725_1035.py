# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20170724_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='help',
        ),
        migrations.AddField(
            model_name='question',
            name='clue',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Clue text'),
        ),
    ]

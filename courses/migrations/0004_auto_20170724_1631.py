# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170724_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningobject',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_object_lesson', to='courses.Lesson', verbose_name='Lesson'),
        ),
    ]
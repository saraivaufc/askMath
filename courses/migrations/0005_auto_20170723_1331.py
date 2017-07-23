# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_answer_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('-creation',), 'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['creation'], 'verbose_name': 'Choice', 'verbose_name_plural': 'Choices'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['position', 'creation'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['position', 'creation'], 'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='introduction',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='question',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='video',
            name='last_modified',
        ),
    ]

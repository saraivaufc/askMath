# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 02:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Level Manager',
                'verbose_name_plural': 'Levels Manager',
            },
        ),
        migrations.CreateModel(
            name='RankingManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Ranking Manager',
                'verbose_name_plural': 'Rankings Manager',
            },
        ),
        migrations.CreateModel(
            name='ScoreManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': [],
                'verbose_name': 'Score Manager',
                'verbose_name_plural': 'Scores Manager',
            },
        ),
    ]
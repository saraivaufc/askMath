# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-11 04:51
from __future__ import unicode_literals

import base.utils.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', base.utils.models.AutoSlugField(blank=True, db_index=False, populate_from=b'title', unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', base.utils.models.AutoSlugField(blank=True, db_index=False, populate_from=b'title', unique=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
                ('categories', models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Categories')),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]

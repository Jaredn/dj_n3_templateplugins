# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 23:01
from __future__ import unicode_literals
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now_add=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('pythonpath', models.CharField(max_length=128, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'ENABLED'), (1, 'DISABLED')])),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]

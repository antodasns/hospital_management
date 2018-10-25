# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-03 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('chart_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=50)),
                ('upper_limit', models.CharField(max_length=50)),
                ('lower_limit', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Chart',
            },
        ),
        migrations.CreateModel(
            name='lab_tech',
            fields=[
                ('tech_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'Lab_technician',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('test_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('chart_id', models.IntegerField()),
                ('patient_user_id', models.IntegerField()),
                ('test_result', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Tests',
            },
        ),
    ]
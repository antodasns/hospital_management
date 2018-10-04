# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-03 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admit',
            fields=[
                ('admit_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('patient_user_id', models.IntegerField()),
                ('admit_date', models.DateField(max_length=50)),
                ('discharge_date', models.DateField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Admit_details',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patient_user_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('patient_name', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=35)),
                ('status', models.CharField(choices=[('1', 'Admitted'), ('2', 'Discharged')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Patient_details',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('report_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('tech_id', models.IntegerField()),
                ('patient_user_id', models.IntegerField()),
                ('test_id', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Reports',
            },
        ),
    ]

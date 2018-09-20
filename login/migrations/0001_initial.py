# Generated by Django 2.1.1 on 2018-09-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=35)),
                ('designation', models.CharField(choices=[('1', 'Admin'), ('2', 'Doctor'), ('3', 'Lab'), ('4', 'Patient')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
    ]

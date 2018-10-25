# Generated by Django 2.1.1 on 2018-10-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0002_tests_test_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('consult_id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('patient_user_id', models.IntegerField()),
                ('doctor_user_id', models.IntegerField()),
                ('suggestions_prescriptions', models.TextField(max_length=500)),
                ('health_tips_diets', models.TextField(max_length=500)),
                ('consult_date', models.DateField(max_length=50, null=True)),
                ('next_consult_dates', models.DateField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Consulting',
            },
        ),
    ]
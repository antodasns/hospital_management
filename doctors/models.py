# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
specialization=(
			('1','Endocrinologists'),
            ('2','Cardio'),
            ('3','ENT specialist'),
            ('4','Eye specialist'),
			)
class Doctor_timing(models.Model):
	timing_id=models.AutoField(max_length=11,primary_key=True)
	available_date=models.DateField(max_length=50)
	available_from=models.TimeField(max_length=50)
	available_to=models.TimeField(max_length=50)
	class Meta:
		verbose_name_plural="Doctor_timing"
	def __str__(self):
		return str(self.timing_id)

class Doctor(models.Model):
	doctor_user_id=models.AutoField(max_length=11,primary_key=True)
	user_id=models.IntegerField()
	timing_id=models.IntegerField()
	doctor_name=models.CharField(max_length=50)
	mobile=models.IntegerField()
	email=models.EmailField(max_length=35)
	photo=models.ImageField()
	specialization=models.CharField(choices=specialization,max_length=1)
	class Meta:
		verbose_name_plural="Doctor_deatails"
	def __str__(self):
		return self.doctor_name

class Appointment(models.Model):
    appointment_id=models.AutoField(max_length=11,primary_key=True)
    patient_user_id=models.IntegerField()
    doctor_user_id=models.IntegerField()
    appointment_date=models.DateField(max_length=50)
    appointment_time=models.TimeField(max_length=50)
    class Meta:
        verbose_name_plural="appointment"


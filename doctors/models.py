# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
specialization=(
			('1','Dermatologist'),
            ('2','Cardio'),
            ('3','ENT specialist'),
            ('4','Eye specialist'),
			)

class Doctor(models.Model):
	doctor_user_id=models.AutoField(max_length=11,primary_key=True)
	user_id=models.IntegerField()
	timing_id=models.IntegerField()
	doctor_name=models.CharField(max_length=50)
	mobile=models.IntegerField()
	email=models.EmailField(max_length=35)
	photo=models.ImageField(max_length=255)
	specialization=models.CharField(choices=specialization,max_length=1)
	class Meta:
		verbose_name_plural="Doctor_deatails"
	def __str__(self):
		return self.doctor_name

'''class Consulting(models.Model):
	consult_id=models.AutoField(max_length=11,primary_key=True)
	patient_user_id=models.IntegerField()
	doctor_user_id=models.IntegerField()
	suggestions_prescriptions=models.TextField(max_length=500)
	health_tips_diets=models.TextField(max_length=500)
	next_consult_dates=models.CharField(max_length=30)
	class Meta:
    	verbose_name_plural="Consulting"
    def __str__(self):
    	return self.consult_id

class Doctor_timing(models.Model):
	timing_id=models.AutoField(max_length=11,primary_key=True)
	doctor_user_id=models.IntegerField()
	date=models.DateField(max_length=50)
	available_from=models.TimeField(max_length=50)
	available_to=models.TimeField(max_length=50)
	class Meta:
    	verbose_name_plural="Doctor_timing"
    def __str__(self):
    	return self.timing_id
'''
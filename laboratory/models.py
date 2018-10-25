# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class lab_tech(models.Model):
	tech_id=models.AutoField(max_length=11,primary_key=True)
	user_id=models.IntegerField()
	name=models.CharField(max_length=50)
	mobile=models.IntegerField()
	email=models.EmailField(max_length=35)
	class Meta:
		verbose_name_plural="Lab_technician"
	def __str__(self):
		return self.name

class Tests(models.Model):
	test_id=models.AutoField(max_length=11,primary_key=True)
	chart_id=models.IntegerField()
	patient_user_id=models.IntegerField()
	test_result=models.CharField(max_length=50)
	test_date=models.DateField(null=True,max_length=50)
	class Meta:
		verbose_name_plural="Tests"
	def __str__(self):
		return str(self.test_id)

class Chart(models.Model):
	chart_id=models.AutoField(max_length=11,primary_key=True)
	test_name=models.CharField(max_length=50)
	upper_limit=models.CharField(max_length=50)
	lower_limit=models.CharField(max_length=50)
	class Meta:
		verbose_name_plural="Chart"
	def __str__(self):
		return self.test_name
class Consulting(models.Model):
	consult_id=models.AutoField(max_length=11,primary_key=True)
	patient_user_id=models.IntegerField()
	doctor_user_id=models.IntegerField()
	suggestions_prescriptions=models.TextField(max_length=500)
	health_tips_diets=models.TextField(max_length=500)
	consult_date=models.DateField(null=True,max_length=50)
	next_consult_dates=models.DateField(max_length=30)
	class Meta:
		verbose_name_plural="Consulting"
	def __str__(self):
		return str(self.consult_id)
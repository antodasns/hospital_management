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
	test_result=models.TextField(max_length=500)
	class Meta:
		verbose_name_plural="Tests"
	def __str__(self):
		return self.test_name

class Chart(models.Model):
	chart_id=models.AutoField(max_length=11,primary_key=True)
	test_name=models.CharField(max_length=50)
	upper_limit=models.CharField(max_length=50)
	lower_limit=models.CharField(max_length=50)
	class Meta:
		verbose_name_plural="Chart"
	def __str__(self):
		return self.test_name
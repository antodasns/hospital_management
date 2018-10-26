# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
status=(
            ('1','Admitted'),
            ('2','Discharged'),
            )

class Patients(models.Model):
	patient_user_id=models.AutoField(max_length=11,primary_key=True)
	user_id=models.IntegerField()
	admit_id=models.IntegerField()
	patient_name=models.CharField(max_length=50)
	dob=models.DateField(max_length=50)
	mobile=models.IntegerField()
	email=models.EmailField(max_length=35)
	
	class Meta:
		verbose_name_plural="Patient_details"
	def __str__(self):
		return self.patient_name

class Reports(models.Model):
	report_id=models.AutoField(max_length=11,primary_key=True)
	tech_id=models.IntegerField()
	patient_user_id=models.IntegerField()
	test_id=models.IntegerField()
	class Meta:
		verbose_name_plural="Reports"
	def __str__(self):
		return self.report_id

class Admit(models.Model):
	admit_id=models.AutoField(max_length=11,primary_key=True)
	status=models.CharField(choices=status,max_length=1)
	admit_date=models.DateField(max_length=50)
	discharge_date=models.DateField(max_length=50)
	class Meta:
		verbose_name_plural="Admit_details"
	def __str__(self):
		return self.admit_id


	
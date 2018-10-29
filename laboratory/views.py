from django.shortcuts import render
from laboratory.formtest import Test
from laboratory.models import Tests,Chart
from doctors.models import Doctor,Appointment
from patients.models import Patients
from django.http import HttpResponse,HttpResponseRedirect
import datetime
import random
import numpy
# Create your views here.

#redirect_home--------------------------------------------------------------------------------------------------------------------------

def index(request):
	if (request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			return HttpResponseRedirect("/laboratory/lab_home")
	else:
		return HttpResponseRedirect("/login/")

#home-----------------------------------------------------------------------------------------------------------------------------

def lab_home(request):
	if (request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			return render(request,'labindex.html')
	else:
		return HttpResponseRedirect("/login/")

#logout-------------------------------------------------------------------------------------------------------------------------

def lab_logout(request):
	try:

		del request.session['lab_username']

		del request.session['password']

	except KeyError:
		pass
	return HttpResponseRedirect("/login/")

#view_patients---------------------------------------------------------------------------------------------------------------------

def pat(request):
	if (request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			get_pat=Patients.objects.all()
			return render(request,'patientnamelab.html',{'pat':get_pat})
	else:
		return HttpResponseRedirect("/login/")

#view_doc-------------------------------------------------------------------------------------------------------------------------

def doc(request):
	if (request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
			return render(request,'doctorlab.html',{'doc':get_doc})
	else:
		return HttpResponseRedirect("/login/")

#view_test_result--------------------------------------------------------------------------------------------------------------------

def result(request):
	if (request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			get_pat=Patients.objects.all()
			get_test=Chart.objects.all()
			return render(request,'test.html',{'pat':get_pat, 'tst':get_test})
	else:
		return HttpResponseRedirect("/login/")

#submit_result/recoment/appointment---------------------------------------------------------------------------------------------------

def submit_result(request):
	if (request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			if request.method == 'POST':

				result=Tests(
				patient_user_id=request.POST.get('patname'),
				chart_id=request.POST.get('testname'),
				test_result=request.POST.get('result'),
				test_date=datetime.date.today())
				result.save()
				chart_id=request.POST.get('testname')
				user_id_pat=Patients.objects.all().filter(pk=request.POST.get("patname"))
				for i in user_id_pat:
					use=i.user_id
					
				#cardio appointment

				if chart_id=='8':
					result=Tests.objects.all().filter(chart_id=8)
					normal=Chart.objects.all().filter(pk=8)
					x=[]
					time_list=['10:00:00','11:00:00','12:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00',]
					month_no=datetime.datetime.now().month
					year_no=datetime.datetime.now().year
					day_no=datetime.datetime.now().day
					day_rand=random.randint(day_no,30)
					
					for a in result:
						res=int(a.test_result)
						
					for b in normal:
						high=int(b.upper_limit)
						low=int(b.lower_limit)
					if res not in range(high,low):
						doc=Doctor.objects.all().filter(specialization=2)
					else:
						return HttpResponse("Normal No Appointment")
					for docs in doc:
						appdoc=docs.doctor_user_id
						x.append(appdoc)
					rand_doc=random.choice(x)
					rand_date=datetime.date(year_no,month_no,day_rand)
					rand_time=random.choice(time_list)
					
					appt=Appointment()	
					appt.doctor_user_id=rand_doc
					appt.patient_user_id=use
					appt.appointment_date=rand_date
					appt.appointment_time=rand_time
					appt.save()
					return HttpResponseRedirect("/laboratory/result/")

					#Endocrinologists

				elif chart_id in ['9','10']:

					c=chart_id
				
					result=Tests.objects.all().filter(chart_id=c)
					normal=Chart.objects.all().filter(pk=c)

					x=[]
					time_list=['10:00:00','11:00:00','12:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00',]
					month_no=datetime.datetime.now().month
					year_no=datetime.datetime.now().year
					day_no=datetime.datetime.now().day
					day_rand=random.randint(day_no,28)
					
					for a in result:
						res=int(a.test_result)
						
					for b in normal:
						high=int(b.upper_limit)
						low=int(b.lower_limit)
					if res not in range(high,low):
						doc=Doctor.objects.all().filter(specialization=1)
					else:
						return HttpResponse("Normal No Appointment")
					for docs in doc:
						appdoc=docs.doctor_user_id
						x.append(appdoc)
					rand_doc=random.choice(x)
					rand_date=datetime.date(year_no,month_no,day_rand)
					rand_time=random.choice(time_list)
					
					appt=Appointment()	
					appt.doctor_user_id=rand_doc
					appt.patient_user_id=use
					appt.appointment_date=rand_date
					appt.appointment_time=rand_time
					appt.save()
					return HttpResponseRedirect("/laboratory/result/")

					#Hematology 

				elif chart_id=='2':
					result=Tests.objects.all().filter(chart_id=2)
					normal=Chart.objects.all().filter(pk=2)
					x=[]
					time_list=['10:00:00','11:00:00','12:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00',]
					month_no=datetime.datetime.now().month
					year_no=datetime.datetime.now().year
					day_no=datetime.datetime.now().day
					day_rand=random.randint(day_no,28)
					
					for a in result:
						res=int(a.test_result)
						
					for b in normal:
						high=int(b.upper_limit)
						low=int(b.lower_limit)
					if res not in range(high,low):
						doc=Doctor.objects.all().filter(specialization=3)
					else:
						return HttpResponse("Normal No Appointment")
					for docs in doc:
						appdoc=docs.doctor_user_id
						x.append(appdoc)
					rand_doc=random.choice(x)
					rand_date=datetime.date(year_no,month_no,day_rand)
					rand_time=random.choice(time_list)
					
					appt=Appointment()	
					appt.doctor_user_id=rand_doc
					appt.patient_user_id=use
					appt.appointment_date=rand_date
					appt.appointment_time=rand_time
					appt.save()
					return HttpResponseRedirect("/laboratory/result/")

					#Hematology 1

				elif chart_id in ['5','4','3','1']:
					d=chart_id

					result=Tests.objects.all().filter(chart_id=d)
					normal=Chart.objects.all().filter(pk=d)
					x=[]
					time_list=['10:00:00','11:00:00','12:00:00','01:00:00','02:00:00','03:00:00','04:00:00','05:00:00','06:00:00',]
					month_no=datetime.datetime.now().month
					year_no=datetime.datetime.now().year
					day_no=datetime.datetime.now().day
					day_rand=random.randint(day_no,28)
					
					for a in result:
						res=float(a.test_result)
						pat=a.patient_user_id
					for b in normal:
						high=float(b.upper_limit)
						low=float(b.lower_limit)
					if res not in numpy.arange(high,low):
						doc=Doctor.objects.all().filter(specialization=3)
					else:
						return HttpResponse("Normal No Appointment")
					for docs in doc:
						appdoc=docs.doctor_user_id
						x.append(appdoc)
					rand_doc=random.choice(x)
					rand_date=datetime.date(year_no,month_no,day_rand)
					rand_time=random.choice(time_list)
					
					appt=Appointment()	
					appt.doctor_user_id=rand_doc
					appt.patient_user_id=use
					appt.appointment_date=rand_date
					appt.appointment_time=rand_time
					appt.save()
					return HttpResponseRedirect("/laboratory/result/")

				else:
					return HttpResponse("no value")

	else:
		return HttpResponseRedirect("/login/")

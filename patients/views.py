from django.shortcuts import render
from doctors.models import Doctor,Doctor_timing
from laboratory.models import Consulting,Tests,Chart
from doctors.models import Appointment
from django.http import HttpResponse,HttpResponseRedirect
import random
import datetime
# Create your views here.
def index(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return HttpResponseRedirect("/patients/pat_home")
	else:
		return HttpResponseRedirect("/login/login/")
def pat_home(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return render(request,'patientindex.html')
	else:
		return HttpResponseRedirect("/login/login/")
def pat_logout(request):
	try:

		del request.session['pat_username']

		del request.session['password']

	except KeyError:
		pass
	return HttpResponseRedirect("/login/login/")
def registration(request):
	
	return render(request,'registration')
def profile(request):
	
	return render(request,'profile.html')

def doc(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
			return render(request,'doc_details.html',{'doc':get_doc})
	else:
		return HttpResponseRedirect("/login/login/")		
def laboratory(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return render(request,'laboratory.html')
	else:
		return HttpResponseRedirect("/login/login/")
def appointment(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return render(request,'myappointment.html')
	else:
		return HttpResponseRedirect("/login/login/")
def labrep(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			get_result=Tests.objects.raw("SELECT * FROM laboratory_tests JOIN laboratory_chart WHERE laboratory_tests.chart_id=laboratory_chart.chart_id")
			return render(request,'labreports.html',{'res':get_result})
	else:
		return HttpResponseRedirect("/login/login/")
def prescribe(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			get_consult=Consulting.objects.all()
			return render(request,'prescribe.html',{'consul':get_consult})
	else:
		return HttpResponseRedirect("/login/login/")
'''def appoint(request):
	result=Tests.objects.all().filter(chart_id=8)

	normal=Chart.objects.all().filter(pk=8)
	x=[]
	time_list=['10:00:00','02:00:00','06:00:00']
	month_no=datetime.datetime.now().month
	year_no=datetime.datetime.now().year
	day_no=datetime.datetime.now().day
	day_rand=random.randint(day_no,28)
	
	for a in result:
		res=int(a.test_result)
		pat=a.patient_user_id
	for b in normal:
		high=int(b.upper_limit)
		low=int(b.lower_limit)
	if res not in range(high,low):
		doc=Doctor.objects.all().filter(specialization=2)
	for docs in doc:
		appdoc=docs.doctor_user_id
		x.append(appdoc)
	rand_doc=random.choice(x)
	rand_date=datetime.date(year_no,month_no,day_rand)
	rand_time=random.choice(time_list)
	
	appt=Appointment()	
	appt.doctor_user_id=rand_doc
	appt.patient_user_id=pat
	appt.appointment_date=rand_date
	appt.appointment_time=rand_time
	appt.save()
	return HttpResponse("success")'''
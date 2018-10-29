from django.shortcuts import render
from doctors.models import Doctor,Doctor_timing
from laboratory.models import Consulting,Tests,Chart
from doctors.models import Appointment
from django.http import HttpResponse,HttpResponseRedirect
import random
import datetime
# Create your views here.

#redirect_home----------------------------------------------------------------------------------------------------------------

def index(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return HttpResponseRedirect("/patients/pat_home")
	else:
		return HttpResponseRedirect("/login/")

#home-------------------------------------------------------------------------------------------------------------------------------

def pat_home(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return render(request,'patientindex.html')
	else:
		return HttpResponseRedirect("/login/")

#logout-------------------------------------------------------------------------------------------------------------------------------

def pat_logout(request):
	try:

		del request.session['pat_username']

		del request.session['password']

	except KeyError:
		pass
	return HttpResponseRedirect("/login/")

#view_doctor------------------------------------------------------------------------------------------------------------------------

def doc(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
			return render(request,'doc_details.html',{'doc':get_doc})
	else:
		return HttpResponseRedirect("/login/")		

#view_laboratory--------------------------------------------------------------------------------------------------------------------

def laboratory(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return render(request,'laboratory.html')
	else:
		return HttpResponseRedirect("/login/")

#appointment----------------------------------------------------------------------------------------------------------------------

def appointment(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			pat=request.session.get('user_in')
			d=[]
			doci=[]
			
			appoint_doc_id=Appointment.objects.all().filter(patient_user_id=pat)
			for a in appoint_doc_id:
				docs_id=a.doctor_user_id
				d.append(a.doctor_user_id)
			for i in d:
				appoint_doc_name=Doctor.objects.values_list('doctor_name',flat=True).get(pk=i)
				doci.append(appoint_doc_name)

			appoint_doc_date=Appointment.objects.all().filter(patient_user_id=pat)
			ziper=zip(appoint_doc_date,doci)
			return render(request,'myappointment.html',{'ziper':ziper})
	else:
		return HttpResponseRedirect("/login/")

#results---------------------------------------------------------------------------------------------------------------------------

def labrep(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			get_result=Tests.objects.raw("SELECT * FROM laboratory_tests JOIN laboratory_chart WHERE laboratory_tests.chart_id=laboratory_chart.chart_id")
			return render(request,'labreports.html',{'res':get_result})
	else:
		return HttpResponseRedirect("/login/")

#prescription_tips----------------------------------------------------------------------------------------------------------------

def prescribe(request):
	if(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			get_consult=Consulting.objects.all()
			return render(request,'prescribe.html',{'consul':get_consult})
	else:
		return HttpResponseRedirect("/login/")

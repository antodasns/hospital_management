from django.shortcuts import render
from patients.models import Patients
from laboratory.models import Consulting

from django.http import HttpResponse,HttpResponseRedirect
from . import views
# Create your views here.

def index(request):
	if (request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			return HttpResponseRedirect("/doctors/doc_home")
	else:
		return HttpResponseRedirect("/login/login/")

def doc_home(request):
	if (request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			return render(request,'doctorindex.html')
	else:
		return HttpResponseRedirect("/login/login/")
def doc_logout(request):
	try:

		del request.session['doc_username']

		del request.session['password']

	except KeyError:
		pass
	return HttpResponseRedirect("/login/login/")
	
def patappointment(request):
	if (request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			return render(request,'event.html')
	else:
		return HttpResponseRedirect("/login/login/")
def consultings(request,id):
	if (request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			consult_pat_name=Patients.objects.values_list('patient_name', flat=True).get(pk=id)
			pat_id=Patients.objects.values_list('patient_user_id', flat=True).get(pk=id)
			return render(request,'consulting.html',{'patname': consult_pat_name,'pat_id':pat_id })
	else:
		return HttpResponseRedirect("/login/login/")
def submit_consult(request,id):
	if (request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			if request.method == 'POST':
				consults=Consulting(
				patient_user_id=id,
				doctor_user_id=id,
				suggestions_prescriptions=request.POST.get('prescribe'),
				health_tips_diets=request.POST.get('tips'),
				consult_date=datetime.date.today(),
				next_consult_dates=request.POST.get('date'))
				consults.save()
			return HttpResponse("success")
	else:
		return HttpResponseRedirect("/login/login/")
def patientview(request):
	if (request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			get_pat=Patients.objects.all()
			return render(request,'patientname.html',{'pat':get_pat})
	else:
		return HttpResponseRedirect("/login/login/")
from django.shortcuts import render
from login.forms import Loginform,Patientreg,Doctorreg
from django.http import HttpResponse,HttpResponseRedirect
from doctors.models import Doctor,Doctor_timing
from laboratory.models import lab_tech
from login.models import users
from patients.models import Patients,Admit
# Create your views here.
def loginhome(request):
	
	return render(request,'loginindex.html')

def login(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			#return HttpResponse("profile page")
			return HttpResponseRedirect("/login/view_pat")
	else:
		if request.method=="POST":

			form=Loginform(request.POST)

			if form.is_valid():

				username1=form.cleaned_data['username']
				password1=form.cleaned_data['password']
				designation1=form.cleaned_data['designation']

				try:

					user_login=users.objects.get(username=username1, password=password1)
					if designation1 == "Admin":
						request.session['password']='TRUE'
						request.session['username']=form.cleaned_data['username']
						request.session['user_in']=user_login.user_id
						return HttpResponseRedirect('/login/view_pat')

					else:

						return HttpResponseRedirect('/login/login/')

				except:
					
					return HttpResponseRedirect('/login/login/')		
			else:
				return HttpResponse("invalid form")
		else:

			form = Loginform()

		return render(request,'adminlogin.html',{'form':form})

def logout(request):
	try:

		del request.session['username']

		del request.session['password']

	except KeyError:
		pass
	return HttpResponseRedirect("/login/login/")
def view_doc(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
			return render(request,'sidebarform/view_doc.html',{'doc':get_doc})
	else:
		return HttpResponseRedirect("/login/login/")
def view_pat(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):		
			get_patient=Patients.objects.raw("SELECT * FROM patients_patients JOIN patients_admit WHERE patients_patients.patient_user_id=patients_admit.patient_user_id")
			return render(request,'sidebarform/view_pat.html',{'pat':get_patient})
	else:
		return HttpResponseRedirect("/login/login/")
def view_lab(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):		
			get_lab=lab_tech.objects.all()[:10]
			return render(request,'sidebarform/view_lab.html',{'lab':get_lab})
	else:
		return HttpResponseRedirect("/login/login/")
	
def formdoc(request):
	form=''
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):

	
			if request.method == 'POST':
				form=Doctorreg(request.POST, request.FILES)
				if form.is_valid():
					doc_deatil=Doctor(
						doctor_name= form.cleaned_data['name'],
						mobile= form.cleaned_data['number'],
						email= form.cleaned_data['email'],
						photo= form.cleaned_data['photo'],
						specialization= form.cleaned_data['specialisation'],
						)
					doc_deatil.save()

					doc_login=users(
						username=form.cleaned_data['username'],
						password=form.cleaned_data['password'],
						designation='2'
						)
					doc_login.save()

					doc_timing=Doctor_timing(
						available_date=form.cleaned_data['available_date'],
						available_from=form.cleaned_data['available_from'],
						available_to=form.cleaned_data['available_to'],
						)
					doc_timing.save()

					return HttpResponse('success')
				else:
					return HttpResponse(form.errors)
			form=Doctorreg()
			return render(request,'sidebarform/formdoctor.html',{'form': form})
#doc details
def formpat(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
	
			form=''
			if request.method == 'POST':
				form=Patientreg(request.POST)
				if form.is_valid():
					patient_detail=Patients(
						patient_name=form.cleaned_data['name'],
						dob=form.cleaned_data['dob'],
						mobile=form.cleaned_data['number'],
						email=form.cleaned_data['email'],
						status=form.cleaned_data['status'],
						)
					patient_detail.save()

					patient_login=users(
						username=form.cleaned_data['username'],
						password=form.cleaned_data['password'],
						designation='4'
						)
					patient_login.save()

					patient_status=Admit(
						admit_date=form.cleaned_data['admit'],
						discharge_date=form.cleaned_data['discharge'],
						)
					patient_status.save()

					return HttpResponse('success')
				else:
					return HttpResponse(form.errors)
			form=Patientreg()
			return render(request,'sidebarform/formpatient.html',{'form': form})

def formlab(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
	
			form=''
			if request.method == 'POST':
				form=Patientreg(request.POST)
				if form.is_valid():
					lab_detail=lab_tech(
						name=form.cleaned_data['name'],
						mobile=form.cleaned_data['number'],
						email=form.cleaned_data['email'],
						)
					lab_detail.save()

					lab_login=users(
						username=form.cleaned_data['username'],
						password=form.cleaned_data['password'],
						designation='3'
						)
					lab_login.save()

					return HttpResponse('success')
				else:
					return HttpResponse(form.errors)
			form=Patientreg()
			return render(request,'sidebarform/formlab.html',{'form': form})
def docview(request):
	get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
	return render(request,'sidebarform/view_doc.html',{'doc':get_doc})
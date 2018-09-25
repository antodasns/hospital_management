from django.shortcuts import render
from login.forms import Loginform,Patientreg,Doctorreg
from django.http import HttpResponse
from doctors.models import Doctor,Doctor_timing
from login.models import users
from patients.models import Patients,Admit
# Create your views here.
def loginhome(request):
	
	return render(request,'loginindex.html')

def login(request):

	form = Loginform()
	return render(request,'adminlogin.html')
def view_doc(request):

	
	return render(request,'sidebarform/view_doc.html')
def view_pat(request):

	
	return render(request,'sidebarform/view_pat.html')
def view_lab(request):

	
	return render(request,'sidebarform/view_lab.html')
	
def formdoc(request):
	form=''
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
	form=''
	if request.method == 'POST':
		form=Patientreg(request.POST)
		if form.is_valid():
			lab_detail=Patients(
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
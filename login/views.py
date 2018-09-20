from django.shortcuts import render
from login.forms import Loginform,Patientreg,Doctorreg
from django.http import HttpResponse
from doctors.models import Doctor
from login.models import users
from doctors.models import Doctor_timing
# Create your views here.
def loginhome(request):
	
	return render(request,'loginindex.html')

def login(request):

	form = Loginform()
	return render(request,'adminlogin.html', {'form': form})
	
def formp(request):
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


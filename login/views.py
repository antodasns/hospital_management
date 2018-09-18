from django.shortcuts import render
from login.forms import Loginform,Patientreg,Doctorreg

# Create your views here.
def loginhome(request):
	
	return render(request,'loginindex.html')

def login(request):

	form = Loginform()
	return render(request,'adminlogin.html', {'form': form})
	
def formp(request):
	form=''
	if request.method == 'POST':
		form=Contactform(request.POST)
		if form.is_valid():
			variable=Doctor(
				name= form.cleaned_data['user_id'],
				address = form.cleaned_data['timing_id'],
				doctor_name = form.cleaned_data['doctor_name'],
				mobile= form.cleaned_data['mobile'],
				email= form.cleaned_data['email'],
				photo= form.cleaned_data['photo'],
				specialization= form.cleaned_data['specialization'],
				)
			variable.save()
	form=Doctorreg()
	return render(request,'sidebarform/formdoctor.html',{'form': form})


from django.shortcuts import render


# Create your views here.
def index(request):

	return render(request,'patientindex.html')
def login(request):
	
	return render(request,'login.html')
def registration(request):
	
	return render(request,'registration')
def profile(request):
	
	return render(request,'profile.html')
def ser(request):
	
	return render(request,'services-9.html')
def doc(request):
	
	return render(request,'doctor.html')
def laboratory(request):
	
	return render(request,'laboratory.html')
def appointment(request):
	
	return render(request,'myappointment.html')
def labrep(request):
	
	return render(request,'labreports.html')
from django.shortcuts import render
from doctors.models import Doctor,Doctor_timing

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
	get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
	return render(request,'doc_details.html',{'doc':get_doc})
	
def laboratory(request):
	
	return render(request,'laboratory.html')
def appointment(request):
	
	return render(request,'myappointment.html')
def labrep(request):
	
	return render(request,'labreports.html')

	
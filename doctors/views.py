from django.shortcuts import render


# Create your views here.

def index(request):
	
	return render(request,'doctorindex.html')

def patappointment(request):
	
	return render(request,'event.html')
def patientname(request):
	
	return render(request,'patientname.html')
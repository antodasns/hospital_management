from django.shortcuts import render


# Create your views here.
def index(request):
	
	return render(request,'labindex.html')

def pat(request):
	
	return render(request,'patientnamelab.html')
def doc(request):
	
	return render(request,'doctorlab.html')

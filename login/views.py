from django.shortcuts import render
from login.forms import Loginform,Patientreg

# Create your views here.
def loginhome(request):
	
	return render(request,'loginindex.html')

def login(request):

	form = Loginform()
	return render(request,'adminlogin.html', {'form': form})
	
def formp(request):
	form=Patientreg()
	return render(request,'sidebarform/formpatient.html',{'form': form})


from django.shortcuts import render


# Create your views here.

def index(request):
	
	return render(request,'doctorindex.html')

def patappointment(request):
	
	return render(request,'event.html')
def patientname(request):
	
	return render(request,'patientname.html')
def consulting(request):
	form=''
	if request.method == 'POST':
		form=Consulting(request.POST)
		if form.is_valid():
			consult=Consulting(
				suggestions_prescriptions= form.cleaned_data['suggetion'],
				health_tips_diets= form.cleaned_data['tips'],
				next_consult_dates= form.cleaned_data['date'],
				)
			consult.save()
	form=Consulting()
	return render(request,'consulting.html',{'form': form})
from django.shortcuts import render
from laboratory.formtest import Test
from laboratory.models import Tests
# Create your views here.
def index(request):
	
	return render(request,'labindex.html')

def pat(request):
	
	return render(request,'patientnamelab.html')
def doc(request):
	
	return render(request,'doctorlab.html')
def test(request):
	form=''
	if request.method == 'POST':
		form=Test(request.POST)
		if form.is_valid():
			test_result=Tests(
				test_result=form.cleaned_data['result'],
				)
			test_result.save()
	form=Test()
	return render(request,'test.html',{'form': form})
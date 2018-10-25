from django.shortcuts import render
from login.forms import Loginform,Patientreg,Doctorreg
from django.http import HttpResponse,HttpResponseRedirect
from doctors.models import Doctor,Doctor_timing
from laboratory.models import lab_tech
from login.models import users
from patients.models import Patients,Admit
# Create your views here.
def loginhome(request):
	
	return render(request,'loginindex.html')

def login(request):
	if (request.session.get('password') and request.session.get('username')):
	
		if (request.session['password']=="TRUE") and (request.session['username']):
			return HttpResponseRedirect("/login/view_pat")
	elif(request.session.get('password') and request.session.get('doc_username')):
		if (request.session['password']=="TRUE") and (request.session['doc_username']):
			return HttpResponseRedirect("/doctors/doc_home")
	elif(request.session.get('password') and request.session.get('lab_username')):
		if (request.session['password']=="TRUE") and (request.session['lab_username']):
			return HttpResponseRedirect("/laboratory/lab_home")
	elif(request.session.get('password') and request.session.get('pat_username')):
		if (request.session['password']=="TRUE") and (request.session['pat_username']):
			return HttpResponseRedirect("/patients/pat_home")
	else:
		if request.method=="POST":

			form=Loginform(request.POST)

			if form.is_valid():

				username1=form.cleaned_data['username']
				password1=form.cleaned_data['password']
				designation1=form.cleaned_data['designation']

				try:

					if designation1 == "Admin":
						user_login=users.objects.get(username=username1, password=password1,designation=designation1)
						request.session['password']='TRUE'
						request.session['username']=form.cleaned_data['username']
						request.session['user_in']=user_login.user_id
						return HttpResponseRedirect('/login/view_pat')	
					
					elif designation1 == "Doctor":
						user_login=users.objects.get(username=username1, password=password1,designation=designation1)
						request.session['password']='TRUE'
						request.session['doc_username']=form.cleaned_data['username']
						request.session['user_in']=user_login.user_id
						return HttpResponseRedirect('/doctors/')
				
					elif designation1 == "Laboratory":
						user_login=users.objects.get(username=username1, password=password1,designation=designation1)
						request.session['password']='TRUE'
						request.session['lab_username']=form.cleaned_data['username']
						request.session['user_in']=user_login.user_id
						return HttpResponseRedirect('/laboratory/')

					elif designation1 == "Patient":
						user_login=users.objects.get(username=username1, password=password1,designation=designation1)
						request.session['password']='TRUE'
						request.session['pat_username']=form.cleaned_data['username']
						request.session['user_in']=user_login.user_id
						return HttpResponseRedirect('/patients/')

					else:

						return HttpResponseRedirect('/login/login/')

				except:
					
					return HttpResponseRedirect('/login/login/')		
			else:
				return HttpResponse("invalid form")
		else:

			form = Loginform()

		return render(request,'adminlogin.html',{'form':form})

def logout(request):
	try:

		del request.session['username']

		del request.session['password']

	except KeyError:
		pass
	return HttpResponseRedirect("/login/login/")
def view_doc(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
			return render(request,'sidebarform/view_doc.html',{'doc':get_doc})
	else:
		return HttpResponseRedirect("/login/login/")
def view_pat(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):		
			get_patient=Patients.objects.raw("SELECT * FROM patients_patients JOIN patients_admit WHERE patients_patients.patient_user_id=patients_admit.patient_user_id")
			return render(request,'sidebarform/view_pat.html',{'pat':get_patient})
	else:
		return HttpResponseRedirect("/login/login/")
def view_lab(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):		
			get_lab=lab_tech.objects.all()[:10]
			return render(request,'sidebarform/view_lab.html',{'lab':get_lab})
	else:
		return HttpResponseRedirect("/login/login/")
	
def formdoc(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			form=''
			if (request.session.get('password') and request.session.get('username')):
				if (request.session['password']=="TRUE") and (request.session['username']):

			
					if request.method == 'POST':
						form=Doctorreg(request.POST, request.FILES)

						if form.is_valid():

							doc_login=users(
								username=form.cleaned_data['username'],
								password=form.cleaned_data['password'],
								designation='2'
								)
							doc_login.save()
							user_latest=users.objects.latest('user_id')
							doc_timing=Doctor_timing(
								available_date=form.cleaned_data['available_date'],
								available_from=form.cleaned_data['available_from'],
								available_to=form.cleaned_data['available_to'],
								)
							doc_timing.save()
							user_time=Doctor_timing.objects.latest('timing_id')
							doc_deatil=Doctor(
								doctor_name= form.cleaned_data['name'],
								mobile= form.cleaned_data['number'],
								email= form.cleaned_data['email'],
								photo= form.cleaned_data['photo'],
								specialization= form.cleaned_data['specialisation'],
								user_id=user_latest.user_id,
								timing_id=user_time.timing_id
								)
							doc_deatil.save()

							return HttpResponse('success')
						else:
							return HttpResponse(form.errors)
					form=Doctorreg()
					return render(request,'sidebarform/formdoctor.html',{'form': form})
	else:
		return HttpResponseRedirect("/login/login/")
	
#doc details
def formpat(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
	
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
	else:
		return HttpResponseRedirect("/login/login/")
	
def formlab(request):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
	
			form=''
			if request.method == 'POST':
				form=Patientreg(request.POST)
				if form.is_valid():
					lab_detail=lab_tech(
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
	else:
		return HttpResponseRedirect("/login/login/")
	
'''def docview(request):
	get_doc=Doctor.objects.raw("SELECT * FROM doctors_doctor JOIN doctors_doctor_timing WHERE doctors_doctor.timing_id=doctors_doctor_timing.timing_id")
	return render(request,'sidebarform/view_doc.html',{'doc':get_doc})'''

#doctor updation
def editdoc(request,id):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			doc_edit_id=Doctor.objects.values_list('doctor_user_id', flat=True).get(pk=id)
			edit_doc_name=Doctor.objects.values_list('doctor_name', flat=True).get(pk=id)
			edit_doc_email=Doctor.objects.values_list('email', flat=True).get(pk=id)
			edit_doc_mobile=Doctor.objects.values_list('mobile', flat=True).get(pk=id)
			edit_specialization=Doctor.objects.values_list('specialization', flat=True).get(pk=id)
			edit_username=users.objects.values_list('username',flat=True).get(pk=id)
			edit_password=users.objects.values_list('password',flat=True).get(pk=id)
			edit_available_date=Doctor_timing.objects.values_list('available_date',flat=True).get(pk=id)
			edit_available_from=Doctor_timing.objects.values_list('available_from',flat=True).get(pk=id)
			edit_available_to=Doctor_timing.objects.values_list('available_to',flat=True).get(pk=id)
			return render(request,'sidebarform/updatedoc.html',{'docs':edit_doc_name,'edit_doc_email':edit_doc_email,
				'edit_doc_mobile':edit_doc_mobile,'edit_specialization':edit_specialization,'use':edit_username,
				'edit_password':edit_password,'edit_available_date':edit_available_date,
				'edit_available_from':edit_available_from,'edit_available_to':edit_available_from,
				'doc_edit_id':doc_edit_id})
	else:
		return HttpResponseRedirect("/login/login/")
	
def updoc(request,id):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			if request.method == 'POST':
				doc_det=Doctor.objects.get(pk=id)
				doc_det.doctor_name=request.POST.get('doctor_name')
				doc_det.email=request.POST.get('email1')
				doc_det.mobile=request.POST.get('mobile_no1')
				doc_det.specialization=request.POST.get('specialise')
				doc_det.save()
				doc_use=users.objects.get(pk=id)
				doc_use.username=request.POST.get('user_name')
				doc_use.password=request.POST.get('pass_word')
				doc_use.save()
				doc_time=Doctor_timing.objects.get(pk=id)
				doc_time.available_date=request.POST.get('avail_date')
				doc_time.available_from=request.POST.get('avail_from')
				doc_time.available_to=request.POST.get('avail_to')
				doc_time.save()
				return HttpResponse('success')
	else:
		return HttpResponseRedirect("/login/login/")
	
def deldoc(request,id):
	if (request.session.get('password') and request.session.get('username')):
		if (request.session['password']=="TRUE") and (request.session['username']):
			doc_det=Doctor.objects.get(pk=id)
			doc_det.delete()
			doc_use=users.objects.get(pk=id)
			doc_use.delete()
			doc_time=Doctor_timing.objects.get(pk=id)
			doc_time.delete()
			return HttpResponse('success')
	else:
		return HttpResponseRedirect("/login/login/")
from itertools import chain
from operator import attrgetter

#laboratory updation
def edit_lab(request,id):
	edit_lab_id=lab_tech.objects.values_list('tech_id', flat=True).get(pk=id)
	edit_lab_name=lab_tech.objects.values_list('name', flat=True).get(pk=id)
	edit_lab_email=lab_tech.objects.values_list('email', flat=True).get(pk=id)
	edit_lab_mobile=lab_tech.objects.values_list('mobile', flat=True).get(pk=id)
	edit_username=users.objects.values_list('username',flat=True).get(pk=id)
	edit_password=users.objects.values_list('password',flat=True).get(pk=id)
	return render(request,'sidebarform/update_lab.html',{'edit_lab_id':edit_lab_id,'edit_lab_name':edit_lab_name,
		'edit_lab_email':edit_lab_email,'edit_lab_mobile':edit_lab_mobile,'edit_username':edit_username,'edit_password':edit_password,})
def up_lab(request,id):
	if request.method == 'POST':
		lab_det=lab_tech.objects.get(pk=id)
		lab_det.name=request.POST.get('lab_name')
		lab_det.email=request.POST.get('email1')
		lab_det.mobile=request.POST.get('mobile_no1')
		lab_det.save()
		lab_use=users.objects.get(pk=id)
		lab_use.username=request.POST.get('user_name')
		lab_use.password=request.POST.get('pass_word')
		lab_use.save()
		return HttpResponse("success")
def del_lab(request,id):
	lab_det=lab_tech.objects.get(pk=id)
	lab_det.delete()
	lab_use=users.objects.get(pk=id)
	lab_use.delete()
	return HttpResponse('success')

#Patient updation
def edit_pat(request,id):
	edit_pat_id=Patients.objects.values_list('patient_user_id', flat=True).get(pk=id)
	edit_pat_name=Patients.objects.values_list('patient_name', flat=True).get(pk=id)
	edit_pat_email=Patients.objects.values_list('email', flat=True).get(pk=id)
	edit_pat_mobile=Patients.objects.values_list('mobile', flat=True).get(pk=id)
	edit_pat_dob=Patients.objects.values_list('dob',flat=True).get(pk=id)
	edit_pat_status=Patients.objects.values_list('status', flat=True).get(pk=id)
	edit_username=users.objects.values_list('username',flat=True).get(pk=id)
	edit_password=users.objects.values_list('password',flat=True).get(pk=id)
	edit_admit=Admit.objects.values_list('admit_date',flat=True).get(pk=id)
	edit_discharge=Admit.objects.values_list('discharge_date',flat=True).get(pk=id)
	return render(request,'sidebarform/update_patient.html',{'edit_pat_id':edit_pat_id,'edit_pat_name':edit_pat_name,
		'edit_pat_email':edit_pat_email,'edit_pat_mobile':edit_pat_mobile,'edit_pat_dob':edit_pat_dob,'edit_pat_status':edit_pat_status,
		'edit_username':edit_username,'edit_password':edit_password,'edit_admit':edit_admit,'edit_discharge':edit_discharge})

def up_pat(request,id):
	if request.method == 'POST':
		pat_get=Patients.objects.get(pk=id)
		pat_get.patient_name=request.POST.get('pat_name')
		pat_get.email=request.POST.get('email1')
		pat_get.dob=request.POST.get('dob')
		pat_get.mobile=request.POST.get('mobile_no1')
		pat_get.status=request.POST.get('status')
		pat_get.save()
		pat_use=users.objects.get(pk=id)
		pat_use.username=request.POST.get('user_name')
		pat_use.password=request.POST.get('pass_word')
		pat_use.save()
		pat_admit=Admit.objects.get(pk=id)
		pat_admit.admit_date=request.POST.get('admit_date')
		pat_admit.discharge_date=request.POST.get('discharge_date')
		pat_admit.save()
		return HttpResponse('success')
def del_pat(request,id):
	pat_det=Patients.objects.get(pk=id)
	pat_det.delete()
	pat_use=users.objects.get(pk=id)
	pat_use.delete()
	pat_admit=Admit.objects.get(pk=id)
	pat_admit.delete()
	return HttpResponse('success')
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

designation= (
('Admin','Admin'),
('Doctor','Doctor'),
('Laboratory','Laboratory'),
('Patient','Patient'),
)

doctors= (
	('','......'),
	('1','Dermatologist'),
	('2','Cardio'),
	('3','ENT Specialist'),
	('4','Eye Specialist'),
	)

status= (
('1','Admitted'),
('2','Discharged'),
)

#user login
class Loginform(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9]+','id':'sample-text-1'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	designation=forms.ChoiceField(choices=designation,widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))

#add patients
class Patientreg(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9]+','id':'sample-text-1'}))
	dob=forms.DateField(widget=forms.DateInput(attrs={'class':'mdl-textfield__input',
		'onfocus':'(this.type="date")','onblur':'(this.type="text")','id':'appointment-date'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	number=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{10}','id':'sample-number-1'}))
	status=forms.ChoiceField(choices=status,widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))
	admit=forms.DateField(widget=forms.DateInput(attrs={'class':'mdl-textfield__input',
		'onfocus':'(this.type="date")','onblur':'(this.type="text")','id':'appointment-date'}))
	discharge=forms.DateField(widget=forms.DateInput(attrs={'class':'mdl-textfield__input',
		'onfocus':'(this.type="date")','onblur':'(this.type="text")','id':'appointment-date'}))

#add doctors
class Doctorreg(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9]+','id':'sample-text-1'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	number=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{10}','id':'sample-number-1'}))
	specialisation=forms.ChoiceField(choices=doctors,widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))
	available_date=forms.DateField(widget=forms.DateInput(attrs={'class':'mdl-textfield__input',
		'onfocus':'(this.type="date")','onblur':'(this.type="text")','id':'appointment-date'}))
	available_from=forms.TimeField(widget=forms.TimeInput(attrs={'class':'mdl-textfield__input',
		'onfocus':'(this.type="time")','onblur':'(this.type="text")','id':'appointment-date'}))
	available_to=forms.TimeField(widget=forms.TimeInput(attrs={'class':'mdl-textfield__input',
		'onfocus':'(this.type="time")','onblur':'(this.type="text")','id':'appointment-date'}))
	photo=forms.FileField()

#add lab_tech
class Labreg(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9]+','id':'sample-text-1'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	number=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{10}','id':'sample-number-1'}))


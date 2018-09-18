from django import forms

designation= (
('1','Admin'),
('2','Doctor'),
('3','Lab_tech'),
('4','Patient'),
)

doctors= (
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
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
	'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	designation=forms.ChoiceField(choices=designation,widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))

#add patients
class Patientreg(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	dob=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{2}/[0-9]{2}/[0-9]{4}','id':'sample-text-1'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	number=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{10}','id':'sample-number-1'}))
	status=forms.ChoiceField(choices=status,widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))
	admit=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{2}/[0-9]{2}/[0-9]{4}','id':'sample-text-1'}))
	discharge=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{2}/[0-9]{2}/[0-9]{4}','id':'sample-text-1'}))


#add doctors
class Doctorreg(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	number=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{10}','id':'sample-number-1'}))
	specialisation=forms.ChoiceField(choices=doctors,widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))
	available_from=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[1-12]{2}:[0-60]{2} [apm]{2}','id':'sample-text-1'}))
	available_to=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[1-12]{2}:[0-60]{2} [apm]{2}','id':'sample-text-1'}))
	available_date=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{2}/[0-9]{2}/[0-9]{4}',
		'id':'sample-text-1'}))

#add lab_tech
class Labreg(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$','id':'login-email'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','id':'login-password'}))
	number=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input',
		'pattern':'[0-9]{10}','id':'sample-number-1'}))


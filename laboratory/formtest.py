from django import forms

class Test(forms.Form):
	patient_name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input','pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	result=forms.CharField(widget=forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5','id':'sample-message-1'}))
	test_name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input','pattern':'[A-Za-z ]+','id':'sample-text-1'}))
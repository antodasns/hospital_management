from django import forms

class Test(forms.Form):
	patient_name=forms.ChoiceField(choices='',widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))
	test_name=forms.ChoiceField(choices='',widget=forms.Select(attrs={'class':'mdl-selectfield__select',
		'id':'sample-selectlist-1'}))
	result=forms.CharField(widget=forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5','id':'sample-message-1'}))

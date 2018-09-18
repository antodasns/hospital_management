from django import forms

class Consulting(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input','pattern':'[A-Za-z ]+','id':'sample-text-1'}))
	suggetion=forms.CharField(widget=forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5','id':'sample-message-1'}))
	tips=forms.CharField(widget=forms.Textarea(attrs={'class':'mdl-textfield__input','rows':'5','id':'sample-message-1'}))
	date=forms.CharField(widget=forms.Textarea(attrs={'class':'mdl-textfield__input','pattern':'[0-9]{2}/[0-9]{2}/[0-9]{4}','id':'sample-text-1'}))
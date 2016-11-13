from django import forms

class MsamForm(forms.Form):
    msam = forms.CharField(label='MSAM number', max_length=9)

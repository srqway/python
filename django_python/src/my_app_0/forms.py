from django import forms


class MyForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    

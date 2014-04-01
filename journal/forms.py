__author__ = 'zdvitas'
from django import forms


class add_task_form(forms.Form):
    tittle = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)

class form_login(forms.Form):
    login = forms.CharField(max_length=200)
    password = forms.PasswordInput()


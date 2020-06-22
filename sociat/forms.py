from django import forms
from sociat.models import Register,profile,set_passwor
from django.forms import ModelForm
#from django.contrib.auth.models import User
class Reg_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Register
        fields=('__all__')
class pro_form(ModelForm):
    class Meta():
        model=profile
        fields=('__all__')
class passw(ModelForm):
    username=forms.CharField()
    new_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=set_passwor
        fields=('__all__')

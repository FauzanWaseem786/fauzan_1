from . import models
from django import forms
from django.forms import ModelForm
from Groups.models import Group
class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields=('__all__')
        exclude =('admins',)

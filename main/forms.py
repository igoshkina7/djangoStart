import email
from django import forms
from django.contrib.auth.models import User
from account.models import LK
from django.forms import ModelForm,  TextInput
from django.forms.models import inlineformset_factory


class Find(forms.Form):
    find=forms.CharField(label="", required=False)


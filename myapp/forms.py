from dataclasses import field, fields
from msilib.schema import Control
from django import forms
from .models import Data

class Registration(forms.ModelForm):
    class Meta:
        model=Data
        fields=['rollno','name','middle','surname','mobileno','email','address','password']
        widgets={
            'rollno':forms.NumberInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'middle':forms.TextInput(attrs={'class':'form-control'}),
            'surname':forms.TextInput(attrs={'class':'form-control'}),
            'mobileno':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }

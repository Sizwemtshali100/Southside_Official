from django import forms
from django.forms import ModelForm
from . models import QAAudit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QA_Forms(ModelForm):
    class Meta:
        model = QAAudit
        fields = ['QA_Audit','PolicyNumber','CaseNumber','AVS','Caller_id','debit_date','start_date','Sales_agent','QA_Outcome','QAC_Correction','KPA','Comment']#

        widgets = {           
            'PolicyNumber':forms.TextInput(attrs={'class':'form-control'}),
            'QA_Audit':forms.Select(attrs={'class':'form-control'}),
            'AVS' : forms.Select(attrs={'class':'form-control'}),
            'CaseNumber' : forms.TextInput(attrs={'class':'form-control'}),
            'Caller_id' : forms.TextInput(attrs={'class':'form-control'}),
            'debit_date': forms.Select(attrs={'class':'form-control'}),
            'start_date': forms.Select(attrs={'class':'form-control'}),
            'Sales_agent' : forms.TextInput(attrs={'class':'form-control'}),
            'QA_Outcome' : forms.Select(attrs={'class':'form-control'}),
            'QAC_Correction' : forms.Select(attrs={'class':'form-control'}),
            'KPA' : forms.Select(attrs={'class':'form-control'}),
            'Comment' : forms.Textarea(attrs={'class':'form-control'}),
        }

class User_Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

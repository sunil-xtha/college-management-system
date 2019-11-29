from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Students
        field = '__all__'
        exclude = ['user']
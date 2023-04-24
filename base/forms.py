from django import forms
from .models import UserComplain

class MyModelForm(forms.ModelForm):
    class Meta:
        model = UserComplain
        fields = ('complain1', 'complain2')  # Add more fields as needed

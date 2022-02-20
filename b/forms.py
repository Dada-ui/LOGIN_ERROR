from django import forms
from b.models import *


class Home_Form(forms.ModelForm):
    class Meta:
        model = Home_Model
        fields = '__all__'

class Login_Form(forms.ModelForm):
    class Meta:
        model = Login_Model
        fields = '__all__'
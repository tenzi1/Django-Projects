from django import forms
from django.core import validators
import re
#defining custom validator or checking size
def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError(("the password is tooooo short"), code='invalid')

#for validating name for string values
def validate_name(value):
    if re.findall('\d', value):
        raise forms.ValidationError(('name should be string character'), code='invalid')
    
class SignUp(forms.Form):
    first_name = forms.CharField(initial='First Name',validators=[validate_name])
    last_name = forms.CharField(validators=[validate_name])
    email = forms.EmailField(help_text='write your email')
    address = forms.CharField(required=False)
    technology = forms.CharField(initial='Django', disabled=True)
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput, validators=[ check_size])
    re_password = forms.CharField(help_text='re enter your password', widget=forms.PasswordInput)

    #for single field validation we use clean_fieldname()
    #password validation
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password
    #for age
    def clean_age(self):
        age = self.cleaned_data['age']
        if (age < 0):
            raise forms.ValidationError(('Negative age is prohibited'), code='invalid')
        return age
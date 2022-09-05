from xml.dom import ValidationErr
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100, help_text='subject of mail')
#     message = forms.CharField(widget=forms.Textarea, help_text='Your message')
#     sender = forms.EmailField(help_text='your email')
#     cc_myself = forms.BooleanField(required=False)

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()
    
#form field default cleaning
from django.core.validators import validate_email

class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalie data to a list of strings."""
        #Return empty list if no input was given
        if not value:
            return []
        return value.split(',')
    
    def validate(self, value):
        '''Checks if value consist only of valid emails'''
        #Use the parent's handling of required fields
        super().validate(value)
        for email in value:
            validate_email(email)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    recipients = MultiEmailField()
    cc_myself = forms.BooleanField(required=False)


    #field specific cleaning for reciepients field
    def clean_recipients(self):
        data = self.cleaned_data['recipients']
        if not 'fred@example.com' not in data:
            raise ValidationErr("you have forgotten about Fred!")
        
        #always return a value to use as cleaned_data even if this method didn't change it.
        return data
        
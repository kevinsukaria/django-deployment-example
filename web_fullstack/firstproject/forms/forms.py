from django import forms
from django.core import validators

def custom_validator(value):
    if value[0].lower != 'z':
        raise forms.ValidationError('NAME MUST START WITH Z')


class FormName(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    verify_email = forms.EmailField(max_length=100,label='Enter your email again',required=True)
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
        validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email!= vmail:
            raise forms.ValidationError('MAKE SURE EMAIL MATCH')

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatacher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")

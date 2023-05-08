from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
class Set_Pass_Form(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'type': 'password',
               'placeholder': 'پسورد  خود را وارد کنید'})
    )
    re_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'type': 'password',
               'placeholder': 'تکرار  خود را وارد کنید'})
    )
    def clean(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise ValidationError('پسورد ها باید مثل هم باشندد')

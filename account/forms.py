from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators
from .models import User

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone_number')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'fullname', 'phone_number', 'file_number', 'is_active', 'is_admin')
def start_white_09(value):
    if value[0] != 0 and value[1] != 9:
        raise ValidationError('یک شماره همراه وارد کنید')

class Login_form(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'type': 'text',
               'placeholder': 'شماره تلفن خود را وارد کنید'}),
        validators=[validators.MaxLengthValidator(11), start_white_09]
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'type': 'password',
               'placeholder': 'پسورد  خود را وارد کنید'})
    )

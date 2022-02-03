from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets
from django.core import validators


from reditapp.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name', 'email', 'phone', 'university',
                  'departMent', 'password')
        labels = {'name': 'Full Name', 'email': "Email", 'departMent': "Department",
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'departMent': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        try:
            match = Registration.objects.get(phone=phone)
        except Registration.DoesNotExist:
            return phone

        raise forms.ValidationError(
            'This Phone Number  is already in use.')

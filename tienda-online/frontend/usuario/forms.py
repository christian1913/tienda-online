from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("No existe una cuenta con esta dirección de correo electrónico.")
        return email
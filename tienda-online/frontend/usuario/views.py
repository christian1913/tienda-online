from django.shortcuts import render

# Paginas

def index(request):

    return render(request, 'frontend/usuario/index.html')


# Funciones

import random
import string

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PasswordResetForm

def generate_reset_token():
    # Genera un token seguro de restablecimiento de contraseña
    letters_and_digits = string.ascii_letters + string.digits
    token = ''.join(random.choice(letters_and_digits) for _ in range(32))
    return token

def send_reset_email(email, token):

    print("enviando mail")

def reset_password(request):
    if request.method == "POST":
        token = generate_reset_token()

        print("enviando mail", token)
        # messages.success(request, 'Se ha enviado un correo electrónico con las instrucciones para restablecer tu contraseña')



    return redirect('inicio')
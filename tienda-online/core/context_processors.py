from django.contrib.auth.forms import AuthenticationForm
from frontend.carrito.models import Carrito
from frontend.usuario.forms import PasswordResetForm


def login_form(request):
    return { 'login_form': AuthenticationForm(), 'form_reset' : PasswordResetForm() }

def cart_count(request):
    session_key = request.session.session_key
    if not session_key:
        # Si no hay una clave de sesión, forzar la creación de una
        request.session.create()
        session_key = request.session.session_key

    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    else:
        carrito, _ = Carrito.objects.get_or_create(session_key=session_key)

    cart_count = carrito.carrito.count()

    return {
        'cart_count': cart_count,
    }
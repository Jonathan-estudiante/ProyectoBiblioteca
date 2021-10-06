from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy

from .models import*
from .forms import*
# Create your views here.


def homepage(request):
    return render(request, "usuarios/ingreso.html")


class UsuarioBlibliotecaCreate(CreateView):
    model = User
    template_name = 'usuarios/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:ingreso')

# Función para entrar si ya estamos registrado


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estás logeado como {usuario}")
                return redirect("usuarios:inicio")
            else:
                messages.error(request, "Usuario o contraseña equivocada")
        else:
            messages.error(request, "Usuario o contraseña equivocada")
    form = AuthenticationForm()
    return render(request, "usuarios/ingreso.html", {"form": form})

# Función para salir de la página

def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("usuarios:homepage")

# Clase para editar un usuario


class EditarUsuario(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('usuarios:user-perfil')
    extra_context = {'formEditUser': form_class}

# Funcíon para editar un usuario


# def usuario_Edit(request, id):
#     usuario = Usuario.objects.filter(id=id)
#     if request.method == 'GET':
#         form = RegistroForm(instance=usuario)
#     else:
#         form = RegistroForm(request.POST, instance=usuario)
#         if form.is_valid():
#             form.save()
#         return redirect('usuarios:user-perfil')
#     return render(request, 'usuarios/editar_usuario.html', {'formEditUser': form})


def verDatos(request):
    userId = request.user.id
    id_user = User.objects.get(id=userId)
    contexto = {
        'id_usuario': id_user,
    }
    return render(request, 'usuarios/perfil_usuario.html', contexto)


def verInicio(request):

    return render(request, 'inicio/inicio.html')


# def update_profile(request):

#     if request.method == 'POST':
#         form = RegistroForm(request.POST)
#         form.user.id = request.user
#         if form.is_valid():
#             form.save()
#             return redirect("usuarios:user-perfil")
#     else:
#         form = RegistroForm()

#     contexto = {'formEditUser': form}
#     return render(request, 'usuarios/editar_usuario.html', contexto)

def verInformacion(request):

    return render(request, 'inicio/informacion.html')

def verTerminos(request):

    return render(request, 'inicio/terminos.html')
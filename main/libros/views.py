from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy

from .models import*
from .forms import*

# Clase para editar un libro


class UpdateBook(UpdateView):
    model = BookModel
    form_class = LibroForm
    template_name = 'libros/edit_book.html'
    success_url = reverse_lazy('usuario:homepage')
    extra_context = {'form_edit_book': form_class}

# Función para agregar un libro


def addBook(request):

    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user
            libro.save()
            return redirect("libros:lista_libros")
            message = "Libro Subido EXITOSAMENTE!"
    else:
        form = LibroForm()
    return render(request, 'libros/add_book.html', {'formSaveBook': form})

# Lista de libros subidos por usuario


def listBooks(request):
    usuar = request.user.id
    libro_usuario = BookModel.objects.filter(usuario=usuar)
    contexto = {
        'usuar': usuar,
        'libro_usuario': libro_usuario,
    }
    return render(request, 'libros/list_book.html', contexto)


def addHistory(request):

    if request.method == 'POST':
        form = HistoryForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user
            libro.save()
            return redirect("libros:lista_historias")
            message = "Libro Subido EXITOSAMENTE!"
    else:
        form = HistoryForm()
    return render(request, 'libros/add_history.html', {'formSaveHistory': form})


def listHistorys(request):
    usuar = request.user.id
    libro_usuario = HistoryModel.objects.filter(usuario=usuar)
    contexto = {
        'usuar': usuar,
        'libro_usuario': libro_usuario,
    }
    return render(request, 'libros/list_history.html', contexto)


def deleteBook(request, id):
    libro = HistoryModel.objects.get(id=id)
    libro.delete()
    return redirect("libros:lista_historias")

# Clase para editar un libro


class UpdateHistory(UpdateView):
    model = HistoryModel
    form_class = HistoryForm
    template_name = 'libros/edit_history.html'
    success_url = reverse_lazy('usuario:lista_historias')

# Funcíon para editar un usuario

# def history_Edit(request, id):
#     usuario = HistoryModel.objects.filter(id=id)
#     if request.method == 'GET':
#         form = HistoryForm(instance=usuario)
#     else:
#         form = HistoryForm(request.POST, instance=usuario)
#         if form.is_valid():
#             form.save()
#         return redirect('usuarios:lista_historias')
#     return render(request, 'libros/edit_history.html', {'form_edit_history': form})

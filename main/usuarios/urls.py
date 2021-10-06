from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', UsuarioBlibliotecaCreate.as_view(), name="registro"),
    path('ingreso/', views.login_request, name="ingreso"),
    path('logout/', views.logout_request, name="logout"),
    url(r'^editar_usuario/(?P<pk>\d+)/$',EditarUsuario.as_view(), name="editar_usuario"),    
    path('perfil/', views.verDatos, name="user-perfil"),
    path('inicio/', views.verInicio, name="inicio"),
    # url(r'^editar/(?P<id>\d+)/$', usuario_Edit, name="editar_usuario"),
    path('information/', views.verInformacion, name="app-information"),
    path('terminos/', views.verTerminos, name="terminos"),
    # path('update/', views.update_profile, name="update"),

  
]
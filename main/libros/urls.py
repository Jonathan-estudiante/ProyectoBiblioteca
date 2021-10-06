from django.urls import path
from django.conf.urls import url

from . import views
from .views import *

app_name = 'libros'

urlpatterns = [
    path('add-book/', views.addBook, name="add-book"),
    # path('lista_libros/<int:id>/', views.listBooks, name="lista_libros"),
    path('lista_libros/', views.listBooks, name="lista_libros"),
    path('add-history/', views.addHistory, name="add-history"),
    path('lista_historias/', views.listHistorys, name="lista_historias"),
    path('delete_book/<int:id>/', views.deleteBook, name='delete_book'),
    url(r'^edit_history/(?P<pk>\d+)/$',UpdateHistory, name='edit_history'),   


]
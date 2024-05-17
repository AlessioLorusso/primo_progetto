from django.urls import path
from .views import *

app_name = 'forms_app'

urlpatterns = [
    path('contattaci/',contatti, name='contatti'),
    path('lista_contatti/',lista_contatti, name='lista_contatti'),
    path('elimina_contatto/<int:pk>',elimina_contatto, name='elimina-contatto'),
    path('modifica_contatto/<int:pk>',modifica_contatto, name='modifica-contatto'),


]
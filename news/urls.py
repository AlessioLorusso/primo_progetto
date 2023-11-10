from django.urls import path
from .views import home, listaArticoli, queryBase


app_name = 'news'

urlpatterns= [
    path('',home, name="homeview"),
    path('lista_articoli/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/',listaArticoli, name="lista_articoli"),
    path('query_base/',queryBase, name="query_base"),


]
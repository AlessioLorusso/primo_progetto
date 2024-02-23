from django.urls import path

from .views import *


app_name = 'news'

urlpatterns= [
    path('',home, name="homeview"),
    path("index_news/", index_news, name="index_news"),
    path("articoli/", articoloDetailView, name="articolo_detail"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("giornalista/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path('lista_articoli/<int:pk>',listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/',listaArticoli, name="lista_articoli_giornalista"),
    path('lista_articoli/',listaArticoli, name="lista_articoli"),
    path('lista_giornalisti/',listaGiornalisti, name="lista_giornalisti"),
    path('query_base/',queryBase, name="query_base"),
    path('lista_giornalisti_api/',giornalisti_list_api, name="giornalisti_list_api"),
    path('giornalista_api/<int:pk>',giornalista_api, name="giornalista_api"),
    path('lista_articoli_api/',articoli_list_api, name="articoli_list_api"),
    path('articolo_api/<int:pk>',articolo_api, name="articolo_api"),
]

from django.urls import path
from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista
from prima_app.views import chi_siamo
from prima_app.views import variabili
from prima_app.views import index

app_name="prima_app"
urlpatterns=[
    path('homepage',homepage, name='homepage'), 
    path('welcome',welcome, name='welcome'), 
    path('lista',lista, name='lista'), 
    path('chi_siamo',chi_siamo, name='chi_siamo'),
    path('variabili',variabili, name='variabili'), 
    path('',index, name='index'), 
]
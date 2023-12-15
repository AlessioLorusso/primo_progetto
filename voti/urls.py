from django.urls import path
from voti.views import *

app_name="voti"
urlpatterns = [
    path('lista_materie',view_a, name='lista_materie'),
    path('lista_voti_assenze',view_b, name='lista_voti_assenze'),  
    path('',index3, name='index3'),

]

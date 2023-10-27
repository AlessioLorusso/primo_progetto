from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
"""
def home(request):
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a+=(art.titolo + "<br>")
    
    for gio in Giornalista.objects.all():
        g+= (gio.nome + "<br>") 

    response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g
    return HttpResponse("<h1> Homepage news!</h1>")"""


def home(request):                                          
    a= []    
    """ creo un vettore di articoli"""                                       
    g= []
    """ creo un vettore di giornalisti"""

    for art in Articolo.objects.all():
        a.append(art.titolo)
        """scorro gli oggetti degli articoli e per ogni articolo prendo il titolo
         e differenza di prima che mandava a capo ogni volta 
         li aggiunge al vettore"""

    for gio in Giornalista.objects.all():
        g.append(gio.nome)
        """scorro gli oggetti dei giornalisti e per ogni giornalista prendo il nome
        e a differenza di prima che li printava andando a capo ora
        li aggiunge al vettore"""
    
    response = str(a) + "<br>" + str(g)
    """ salvo le visualizzazioni dei due vettori in una variabile ed 
    è un metodo più efficiente per visualizzare rispetto al precedente"""
    print(response)
    return HttpResponse("<h1>" + response + "</h1>")




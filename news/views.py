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

def listaArticoli(request, pk):
    articoli= Articolo.objects.filter(giornalista_id=pk)
    context= {
        'articoli': articoli,
    }
    return render(request,'lista_articoli.html',context)

def listaArticoli(request, pk=None):
    if(pk==None):
        articoli= Articolo.objects.all()
    else:
        articoli= Articolo.objects.filter(giornalista_id=pk)
    context= {
        'articoli': articoli,
    }
    return render(request,'lista_articoli.html',context)

def queryBase(request):
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi')
    numero_totali_articoli= Articolo.objects.count()

    giornalista_1= Giornalista.objects.get(id=1)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()

    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    articolo_piu_visualizzato = Articolo.objects.order_by('visualizzazioni').first()

    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datatime.date(1900,1,1))

    articoli_del_giorno= Articolo.objects.filter(dara=datatime.date(2023,1,1))

    articoli_periodo = Articolo.objects.filter(data__range=(datatime.date(2023,1,1), datatime.date(2023,12,31)))

    giornalisti_nati=Giornalista.objects.filter(anno_di_nascita__lt=datatime.date(1980,1,1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    giornalista_giovane= Giornalista.objects.order_by('anno_di_nascita').first()

    giornalista_anziano= Giornalista.objects.order_by('-anno_di_nascita').first()

    ultimi= Articolo.objects.order_by('-data')[:5]

    articoli_minime_visualizzazioni= Articolo.objects.filter(visualizzazioni__gte=100)

    articoli_parola = Articolo.objects.filter(titolo__incontais='importante')

    context = {
        'articoli_cognome':articoli_cognome,
        'numero_totali_articoli': numero_totali_articoli,
        'giornalista_1': giornalista_1,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'giornalisti_nati': giornalisti_nati,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
    }
    return render(request,'query.html', context)
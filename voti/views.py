from django.shortcuts import render
from .models import Materia, Voti


# Create your views here.
#
#def viw_a(request){
  #  dizionario={}
   # materie=["Matematica", "Fisica","Chimica","Arte"]

#}

#def queryBase(request){

#}
def index3(request):
    return render(request,"index3.html")

def home(request):
     materie = Materia.objects.all()
     voto = Voti.objects.all()
     context = {"materie": materie, "voto":voto}
     print (context)
     return render(request, "homenews.html", context)

def view_a(request):
    context= {
        'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request,'lista_materie.html',context)

def view_b(request):
      context={
           'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
      }
      return render(request,'lista_voti_assenze.html',context)



#def view_c(request):
     
 #   m=0
  #  sommaVoti=0
    #i=1
    #for i in range('voti'):
     #   listaN.append(n)
      #  m+=n
    #m=m/30
    #context={
     #   'listaN': listaN,
      #  'm':m,
    #}
    #return render(request,'media_voti.html',context)
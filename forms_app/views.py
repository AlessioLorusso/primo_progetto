from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContatto
from .models import Contatto
from django.shortcuts  import get_object_or_404,redirect

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required
# Create your views here.
def contatti(request):

    #Se la richiesta è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":

        #Creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        #is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            #a questo punto possiamo usare i dati validi!
            #tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Il Form è Valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            # ringrazio l'utente per averci contattato - volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
        
        # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo , allora creo il form di default vuoto
    else:
        form = FormContatto()
        
        #arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta (con metodo GET) , o se il form non è valido e ha errori
        context = {"form": form}
        return render(request,"contatto.html",context)
    

def lista_contatti(request, pk=None):
    if(pk==None):
        contatti= Contatto.objects.all()
    else:
        contatti= Contatto.objects.filter(contatto_id=pk)
    context= {
        'contatti': contatti,
    }
    return render(request,'lista_contatti.html',context)


"""
@login_required
è un decorator utilizzato per proteggere le views e garantire che solo gli utenti autenticati possano utilizzarla.
I decorator consentono di modificare il comportamento di una funzione o di una classe senza modificarne il codice interno.
In questo caso aggiunge la funzionalità aggiuntive di permettere la modifica solo ad un utente loggato
"""
@login_required(login_url="/accounts/login")

def modifica_contatto(request, pk):
    # preleva dal database l'oggetto la cui chiave primaria è passata come parametro
    contatto = get_object_or_404(Contatto, id=pk)
    """
    Se l'oggetto non viene trovato, get_object_or_484 restituisce una pagina di errore HTTP 484 (pagina non trovata).
    """
    """
    In Django, ci sono principalmente due tipi di richieste HTTP che una view può gestire: GET e POST.
    Le richieste GET sono utilizzate per recuperare dati dal server,
    mentre le richieste POST sono utilizzate per inviare dati al server,
    ad esempio quando si invia un modulo HTML come in questo caso.
    """

    if request.method == "GET": #prima chiamata get per caricare il form
        form = FormContatto (instance=contatto) #al construttore del form passo il contatto prelevato dal db 
    if request.method=="POST": #seconda chiamata post per modificare il contatto
        form = FormContatto(request.POST, instance=contatto) #ora passo oltre al contatto prelevato dal db anche i dati modificati 
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista_contatti') # url che reindirizza alla pagina lista_contatti.html
    context={'form': form, 'contatto': contatto}
    return render(request, 'modifica_contatto.html', context)

#DECORATORE CHE permette di cancellare il contatto solo ad un utente admin
@staff_member_required(login_url="/accounts/login")
def elimina_contatto (request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST": # vuol dire che l'utente ha inviato il form che conferma l'eliminazione 
        contatto.delete() #elimina il contatto dal database
        return redirect('forms_app:lista_contatti')
    context= {'contatto': contatto}
    return render(request, 'elimina_contatto.html',context)


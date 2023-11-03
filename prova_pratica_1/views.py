from django.shortcuts import render
# Create your views here.
import random

def Index_1(request):
    return render(request,"Index_1.html")

def somma(request):
    
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    context={
        'n1' : n1,
        'n2' : n2,
        'n3' : n1+n2,
    }
    return render(request,"maxmin.html",context)

def media(request):
    m=0
    listaN=[]
    i=1
    for i in range(30):
        n=random.randint(1, 10)  
        listaN.append(n)
        m+=n
    m=m/30
    context={
        'listaN': listaN,
        'm':m,
    }
    return render(request,"media.html",context)

def voti(request):
    context={
        'my_dict': {'studente1': 8, 'studente2': 7 , 'studente3': 4, 'studente4': 9}
    }
    return render(request,"voti.html",context)
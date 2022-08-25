from django.shortcuts import render
from .models import Hermano, Novia, Madre

def familia(request):
    novia = Novia(nombre="Paola", documento=38215606, fecha_nacimiento= "1991-03-30")
    contexto = {'familia': novia}
    novia.save()
    return render(request,"templates.html", contexto)

def familia1(request):
    madre = Madre(nombre1="Silvina", documento1=22354170, fecha_nacimiento1= "1972-04-23")
    contexto1 = {'familia1': madre}
    madre.save()
    return render(request,"templates.html", contexto1)

def familia2(request):
    hermano = Hermano(nombre2="Fede", documento2=43568966, fecha_nacimiento2= "1997-10-01")
    contexto2 = {'familia2': hermano}
    hermano.save()
    return render(request,"templates.html", contexto2)

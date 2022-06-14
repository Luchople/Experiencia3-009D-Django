from django.shortcuts import render, redirect

# Create your views here.
def indexd(request):
    return render (request, 'indexd.html')

def QuienesSomos(request):
    return render (request, 'QuienesSomos.html')

def contacto(request):
    return render (request, 'contacto.html')

def galeria(request):
    return render (request, 'galeria.html')

def peliculasAPI(request):
    return render (request, 'peliculasAPI.html')

def formularioRegistro(request):
    return render (request, 'formularioRegistro.html')
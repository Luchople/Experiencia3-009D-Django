from django.urls import path 
from .views import indexd, QuienesSomos, contacto, galeria, formularioRegistro, peliculasAPI

urlpatterns =[
    path ('/', indexd, name="indexd"),

    path ('QuienesSomos', QuienesSomos, name="QuienesSomos"),

    path ('contacto', contacto, name="contacto"),

    path ('galeria', galeria, name="galeria"),

    path ('peliculasAPI', peliculasAPI, name="peliculasAPI"),

    path ('formularioRegistro', formularioRegistro, name="formularioRegistro"),



    
]



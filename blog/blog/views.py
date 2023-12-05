# render
from django.shortcuts import render

# Portada de pagina

def Home(request):
    return render(request, "Inicio.html")



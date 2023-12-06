from django.shortcuts import render

# Create your views here.

def categorias(request):
    return render(request, "categoria.html")

def post(request):
    return render(request, "post.html")
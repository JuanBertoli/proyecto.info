from django.shortcuts import render
from .models import *
# Create your views here.

def categorias(request):
    return render(request, "categoria.html")

def post(request):
    return render(request, "post.html")

def post_publicado(request):
    posteos = Post.objects.all()
    return render (request, "post.html", {"posteos": posteos})
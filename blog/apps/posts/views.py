from django.shortcuts import render
from .models import *
# Create your views here.

def categorias(request):
    return render(request, "posts/categorias.html")

def post(request):
    return render(request, "posts/post.html")

def post_realizado(request):
    posteos = Post.objects.all()
    return render(request, "posts/post.html", {"posteos": posteos})
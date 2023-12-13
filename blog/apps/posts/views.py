from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def inicio_post(request):
    return render(request, "inicio.html")

def categorias_post(request):
    return render(request, "posts/categorias.html")

# def post(request):
#     return render(request, "posts/post.html")

def posts(request):
    # posteos = Post.objects.all()
    # categorias = Categoria.objects.all()
    # print(categorias)
    # print(posteos)
    id_categoria = request.GET.get('id', None)
    if id_categoria:
        posteos = Post.objects.filter(categoria_post=id_categoria)
    else:
        posteos = Post.objects.all()

    categorias = Categoria.objects.all()
    ctx = zip(posteos, categorias)

    return render(request, "posts/post.html", {"ctx": ctx, "posteos": posteos})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    return render(request, "posts/post_detail.html", ctx)
from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import Formulario_Modificacion

# Create your views here.

def inicio_post(request):
    ctx = {}
    posteos = Post.objects.filter().order_by('-id')[:3]
    ctx['trending']=posteos
    return render(request, "inicio.html", ctx)

def categorias_post(request):
    categorias = Categoria.objects.all()
    ctx = {'categorias':categorias}
    return render(request, "posts/categorias.html", ctx)

def posts(request):

    id_categoria = request.GET.get('id', None)
    if id_categoria:
        posteos = Post.objects.filter(categoria=id_categoria)
    else:
        posteos = Post.objects.all()

    categorias = Categoria.objects.all()
    # ctx = zip(posteos, categorias)

    return render(request, "posts/post.html", {"categorias": categorias, "posteos": posteos})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    return render(request, "posts/post_detail.html", ctx)

def comentar_posteo(request):
    comentario = request.POST.get("comentario", None)
    usuario = request.user
    post = request.POST.get("id_post", None)
    posteo = Post.objects.get(id=post)
    setear_comentario = Comentario.objects.create(
        usuario = usuario,
        post = posteo,
        texto = comentario,
    )
    return redirect("posts:post_detail", post_id=post)

class Borrar_Comentario(DeleteView):
    model = Comentario
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("posts:posts")

class Modificar_Comentario(UpdateView):
    model = Comentario
    form_class = Formulario_Modificacion
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("posts:posts")
from django.urls import path

# importar views
from . import views

app_name= "posts"

urlpatterns = [
    path("", views.inicio_post, name="Inicio"),
    path("categorias/", views.categorias_post, name="categorias"),
    path("posts/", views.posts, name="posts"),
    path("post_detail/<int:post_id>", views.post_detail, name="post_detail"),
    path("comentario", views.comentar_posteo, name="comentar"),
]

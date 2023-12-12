from django.urls import path

# importar views
from . import views

app_name= "posts"

urlpatterns = [
    path("", views.inicio_post, name="Inicio"),
    path("categorias/", views.categorias_post, name="Categorias"),
    path("posts/", views.posts, name="Posts"),
    path("post_detail/<int:post_id>/", views.post_detail, name="Post_Detalles"),
]

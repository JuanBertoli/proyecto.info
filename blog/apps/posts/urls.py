from django.urls import path

# importar views
from . import views

app_name= "posts"

urlpatterns = [
    path("categoria", views.categorias),
    path("post", views.post),
]

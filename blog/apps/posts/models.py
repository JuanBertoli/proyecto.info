from django.db import models
from django.utils import timezone

# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    
    def __str__(self) -> str:
        return self.nombre
class Post(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    
from django.db import models

# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    
    def __str__(self) -> str:
        return self.nombre
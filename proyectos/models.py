from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    link = models.URLField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class punto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='imagen', null=True)
    descripcion = models.TextField(max_length=200, verbose_name='descripcion')

    def __str__(self):
        fila = "nombre: " + self.nombre + "-" + "descripcion: " + self.descripcion
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

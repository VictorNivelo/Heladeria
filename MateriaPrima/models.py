from django.db import models


class MateriaPrima(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_materia = models.CharField(max_length=100)
    cantidad_producto = models.CharField(max_length=100)


    def __str__(self):
        return self.precio_materia

    def listar_MateriaPrima(self):
        return self.objects.all()
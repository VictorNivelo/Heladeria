from django.db import models


class DatosUsuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    cedula_usuario = models.CharField(max_length=11, help_text="Maximo 11 numeros, sin - ")
    numerocelular_usuario = models.CharField(max_length=10, help_text="Maximo 10 numeros con el 0 ")
    direccion_usuario = models.CharField(max_length=100, help_text="Direccion Actual")
    Factura = models.ForeignKey('Factura', on_delete=models.CASCADE, related_name='DatosUsuario_list')


    def __str__(self):
        return self.nombre_usuario

    def listar_DatosUsuario(self):
        return self.objects.all()

class Factura(models.Model):
    NombreLocal = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    Local = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Ruc = models.CharField(max_length=50)
    Factura = models.PositiveIntegerField(null=True, blank=True, help_text="Eliga la cantidad a comprar")

    def __str__(self):
        return self.NombreLocal

    def listar_Factura(self):
        return self.objects.all()

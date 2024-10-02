from django.db import models


class EmpresaHeladeria(models.Model):
    NombreLocal = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    Local = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    Ruc = models.CharField(max_length=50)
    Factura = models.PositiveIntegerField(null=True, blank=True, help_text="Eliga la cantidad a comprar")

    def __str__(self):
        return self.NombreLocal

    def listar_Heladeria(self):
        return self.objects.all()

class Helado(models.Model):
    sabor_Helado = models.CharField(max_length=50)
    precio_Helado = models.CharField(max_length=50)
    cantidad_Helado = models.PositiveIntegerField(null=True, blank=True, help_text="Eliga la cantidad a comprar")
    EmpresaHeladeria = models.ForeignKey('EmpresaHeladeria', on_delete=models.CASCADE, related_name='Helado_list')

    def __str__(self):
        return self.sabor_Helado

    def listar_Helados(self):
        return self.objects.all()

class Cono(models.Model):
    sabor_Cono = models.CharField(max_length=50)
    precio_Cono = models.CharField(max_length=50)
    cantidad_Cono = models.PositiveIntegerField(null=True, blank=True, help_text="Eliga la cantidad a comprar")
    # EmpresaHeladeria = models.ForeignKey('EmpresaHeladeria', on_delete=models.CASCADE, related_name='Cono_list')

    def __str__(self):
        return self.sabor_Cono

    def listar_Conos(self):
        return self.objects.all()

class Galleta(models.Model):
    sabor_Galleta = models.CharField(max_length=100)
    precio_Galleta = models.CharField(max_length=100)
    cantidad_Galleta = models.PositiveIntegerField(null=True, blank=True, help_text="Eliga la cantidad a comprar")
    # EmpresaHeladeria = models.ForeignKey('EmpresaHeladeria', on_delete=models.CASCADE, related_name='Galleta_list')

    def __str__(self):
          return self.sabor_Galleta

    def listar_Galletas(self):
        return self.objects.all()

class Pastel(models.Model):
    sabor_Pastel = models.CharField(max_length=100)
    precio_Pastel = models.CharField(max_length=100)
    cantidad_Pastel = models.PositiveIntegerField(null=True, blank=True, help_text="Eliga la cantidad a comprar")
    # EmpresaHeladeria = models.ForeignKey('EmpresaHeladeria', on_delete=models.CASCADE, related_name='Pastel_list')

    def __str__(self):
        return self.sabor_Pastel

    def listar_Pastel(self):
        return self.objects.all()




from django.contrib import admin
from Heladeria.models import Helado, Cono, Pastel, Galleta, EmpresaHeladeria


class HeladoAdmin(admin.ModelAdmin):
    list_display = ('sabor_Helado', 'precio_Helado', 'cantidad_Helado')
    search_fields = ('sabor_Helado', )
    list_filter = ('EmpresaHeladeria',)

class HeladoInLine(admin.TabularInline):
    model = Helado
    extra = 1

class ConoAdmin(admin.ModelAdmin):
    list_display = ('sabor_Cono', 'precio_Cono', 'cantidad_Cono')
    search_fields = ('sabor_Cono', )
    # list_filter = ('EmpresaHeladeria', )

class ConoInLine(admin.TabularInline):
    model = Cono
    extra = 1

class GalletaAdmin(admin.ModelAdmin):
    list_display = ('sabor_Galleta', 'precio_Galleta', 'cantidad_Galleta')
    search_fields = ('sabor_Galleta', )
    # list_filter = ('Empresa Heladeria', )

class GalletaInLine(admin.TabularInline):
    model = Galleta
    extra = 1


class PastelAdmin(admin.ModelAdmin):
    list_display = ('sabor_Pastel', 'precio_Pastel', 'cantidad_Pastel')
    search_fields = ('sabor_Pastel', )
    # list_filter = ('Empresa Heladeria', )

class PastelInLine(admin.TabularInline):
    model = Pastel
    extra = 1

class EmpresaHeladeriaAdmin(admin.ModelAdmin):
    list_display = ('NombreLocal','Direccion','Local','Telefono','Ruc','Factura')
    search_fields = ('NombreLocal',)
    inlines = (HeladoInLine,)


admin.site.register(Helado,HeladoAdmin)
admin.site.register(Cono,ConoAdmin)
admin.site.register(Galleta,GalletaAdmin)
admin.site.register(Pastel,PastelAdmin)

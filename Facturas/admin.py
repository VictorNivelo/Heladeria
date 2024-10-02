from Facturas.models import DatosUsuario, Factura
from django.contrib import admin

class DatosUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'cedula_usuario', 'numerocelular_usuario','direccion_usuario')
    search_fields = ('nombre_usuario', )
    list_filter = ('Factura',)

class DatosUsuarioInLine(admin.TabularInline):
    model = DatosUsuario
    extra = 1

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('NombreLocal','Direccion','Local','Telefono','Ruc','Factura')
    search_fields = ('NombreLocal',)
    inlines = (DatosUsuarioInLine,)

admin.site.register(DatosUsuario,DatosUsuarioAdmin)
admin.site.register(Factura, FacturaAdmin)


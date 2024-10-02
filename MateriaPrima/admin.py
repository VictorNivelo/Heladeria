from MateriaPrima.models import MateriaPrima
from django.contrib import admin

class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio_materia','cantidad_producto')
    search_fields = ('nombre_producto', )


class MateriaPrimaInLine(admin.TabularInline):
    model = MateriaPrima
    extra = 1

admin.site.register(MateriaPrima,MateriaPrimaAdmin)
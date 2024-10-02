from django.apps import AppConfig


class FacturacionConfig(AppConfig): #CamelCase
    default_auto_field = 'django.db.models.BigAutoField' #snake_case
    name = 'Facturas'
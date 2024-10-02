from django.apps import AppConfig


class HeladeriaConfig(AppConfig): #CamelCase
    default_auto_field = 'django.db.models.BigAutoField' #snake_case
    name = 'Heladeria'

# import django.apps.AppConfig;
#
# public_class PruebaConfig extends AppConfig {
#
#     public String defaultAutoField = "django.db.model.BigAutoField";
#     public String name = "prueba";
# }
from django.apps import AppConfig

#   Configuración de nuestra aplicación
class MiappConfig(AppConfig):
    name = 'miapp'
    verbose_name = 'Mi primera aplicación'  #  Modificar junto con settings.py para que tome verbose_name

from django.contrib import admin
from .models import Article
from .models import Category

# Register your models here. ---Es necesario registrar abajo los módulos a usar para que genere un tipo CRUD---

#  Uso de una clase para visualizar los campos de solo lectura
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

#  Adicionalmente a las tablas que se visualizarán en el Admin de Django pasaremos los campos de solo lectura
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#  Configurar el título del panel de administración general de Django
title = "Plataforma Highbrow"
admin.site.site_header = "Highbrow"
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"
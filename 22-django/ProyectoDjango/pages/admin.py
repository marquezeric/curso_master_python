from django.contrib import admin
from .models import Page

#  Configuración Extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
    search_fields=('title','content')  #  Buscador dentro de mi página por título o contenido
    list_filter=('visible',)
    list_display=('title','visible','created_at')
    ordering=('created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)
    

#  Configuración del panel de gestión
title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle

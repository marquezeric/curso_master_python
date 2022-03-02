from django.contrib import admin

# Register your models here.
# Registra los modelos si los quieres visualizar dentro del Admin de Django

from .models import Customer,Product,Order,Tag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
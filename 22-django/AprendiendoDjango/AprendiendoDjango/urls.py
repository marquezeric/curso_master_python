"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    3. Agregar una URL  en urlpatterns: path('ruta_navegador', views.ejecuta_metodo, name="nombre" )-----------
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings  #  Para el trabajo con imágenes

#  Importar app con mis vistas
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('hola_mundo/', views.hola_mundo, name="hola_mundo"),
    path('pagina-pruebas/', views.pagina, name="pagina"),
    path('pagina-pruebas/<int:redirigir>', views.pagina, name="pagina"),
    path('contacto/',views.contacto, name="Contacto"),
    #  Con paso de parámetros opcionales, con cada uno de los casos que podemos tener
    path('contacto/<str:nombre>',views.contacto, name="Contacto"),
    path('contacto/<str:nombre>/<str:apellidos>',views.contacto, name="Contacto"),
    #path('crear-articulo/', views.crear_articulo, name="crear_articulo"),
    #  Con paso de parámetros para guardar en nuestra base de datos
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('mostrar-articulo/', views.mostrar_articulo, name="mostrar_articulo"),
    #  path editar-articulo indicando el parametro id (se le debe de poner, cuando se teclee el path en la web)
    path('editar-articulo/<int:id>', views.editar_articulo),
    path('listar-articulos/', views.listar_articulos, name = "listar-articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar_articulo"),
    path('guarda-articulo', views.guardar_articulo, name="guarda"),
    path('crea-articulo/', views.crea_articulo, name="crea"),
    path('crea-articulo-completo/', views.crea_articulo_completo, name="crea_completo")
]

#  Configuración cargar imágenes, solo en modo DEBUG, de lo contrario (Producción) no será necesario
#  Trabaja en conjunto con el archivo ---settings.py---
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
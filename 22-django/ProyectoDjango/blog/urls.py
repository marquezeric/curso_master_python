from django.urls import path
from . import views


urlpatterns = [
    path('articulos/', views.list, name = 'Listado_articulos'),
    path('categoria/<int:category_id>', views.categorie, name = "category"),
    path('articulo/<int:article_id>', views.article,name="article")
]
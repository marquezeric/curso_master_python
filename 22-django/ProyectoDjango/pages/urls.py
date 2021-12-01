from django.urls import path
from . import views
#  la variable de abajo es necesario que se llame de esta manera urlpatterns
urlpatterns = [
    path('pagina/<str:slug>', views.page, name="page")
]
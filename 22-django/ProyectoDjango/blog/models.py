from django.db import models
from ckeditor.fields import RichTextField
#  Relación con el modelo Auth, este no se encuentra aquí, para saber que usuario realizó o modificó algo
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:  #  Esta clase nos sirve para cuando se hace mención a la información que maneja la clase lo haga en singular o plural respectivamente
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    #  Este método nos sirve para visualizar el nombre del objeto  la propiedad name
    def __str__(self):
        
        return self.name

class Article(models.Model):
    title = models.CharField(max_length= 150, verbose_name='Título')
    content = RichTextField(verbose_name = 'Contenido')
    image = models.ImageField(default='null', verbose_name = 'Imágen', upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User, editable= False, verbose_name='Usario', on_delete=models.CASCADE)  #  Campo para mostrar los datos del usuario
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank=True, related_name='articles')  #  Relación con el modelo Category
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Editado el')

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at']
 
    def __str__(self):

        return self.title
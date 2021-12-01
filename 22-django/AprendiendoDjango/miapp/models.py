from django.db import models

#  Los Modelos dentro de Django deben tener de preferencia nombres en particular (Singular)
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Título")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(default='null', verbose_name = "Imágen", upload_to = "articles")
    public = models.BooleanField(verbose_name = "Publicado")
    created_at =models.DateTimeField(auto_now_add=True, verbose_name = "Creado el ")
    updated_at =models.DateTimeField(auto_now=True, verbose_name="Modificado el ")
#  Uso de la clase Meta para que Django lo interprete en singular y plurar de acuerdo al lugar en que se encuentre
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering=["id"]  #  Uso de ordering, solo afecta lo del panel Django no lo que se tiene programado con Python

#  Método mágico para que muestre el nombre real del registro y No el del objeto
    
#    def __str__(self):
#        return self.title

#  Método mágico para que muestre el nombre real del registro y No el del objeto

#    def __str__(self):

#        return f"{self.title} creado el {self.created_at} es {self.public}"

#  Método mágico para que muestre el nombre real del registro y No el del objeto, condicionado
    def __str__(self):

        if self.public:
            public = " - Publicado"
        else:
            public = " - Privado"

        return f"{self.title} {public}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
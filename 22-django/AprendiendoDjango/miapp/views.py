from django.http import response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from miapp.models import Article
from django.db.models import Q #  Trabajar con instrucciones SQL
from miapp.forms import FormArticle  #  Importamos de (miapp) de forms.py la clase FormArticle
from django.contrib import messages  #  Importar las librerías para el uso de mensajes


# Create your views here.
#  MVC  (MODELO VISTA CONTROLADOR -> Acciones (Métodos))
#  MVT  (MODELO TEMPLATE VISTA  -> Acciones (métodos))
#  Recordar agregar nuestra "miapp" al archivo de settings.py ------------------------

layout = """

    <h1>Sitio Web con Django | Eric Márquez Salas</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola_mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Página de Pruebas</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Página de Pruebas</a>
        </li>
        <li>
            <a href="/contacto">Siempre en contacto</a>
        </li>
    </ul>
    <hr/>
"""

#def inicio(request):
#    html = """
#        <h1>Inicio</h1>
#       <p>Años hasta el 2050</p>
#        <ul>
#   """
#    year = 2021
#    while year <= 2050:
#        if year % 2 == 0:
#            html += f"<li>{str(year)}</li>"
#        
#        year += 1

#    html += "</ul>"
#   return HttpResponse(layout+html)"""

def inicio(request):
    
    """
    html = ""  #Tenía triple doble comilla
        <h1>Inicio</h1>
       <p>Años hasta el 2050</p>
        <ul>
   ""

    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        
        year += 1

    html += "</ul>"
    """
    year = 2021
    hasta = range(year,2051)

    nombre = 'Eric Márquez'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C#']
#    lenguajes = []

    return render(request, 'inicio.html', {
        'title': 'Home',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years' : hasta

    })

#def hola_mundo(request):
#    return HttpResponse(layout+"""
#        <h1>Hola Estamos Aprendiendo Django</h1>
#        <h3>Soy Eric Márquez Salas</h3>
#    """)

def hola_mundo(request):
    return render(request, 'hola_mundo.html')


#def pagina(request, redirigir = 0):
    
#    if redirigir ==1:
#        #return redirect('/contacto/')
#        #return redirect('/contacto/Juan/Rivera')
#        return redirect('Contacto', nombre = "Ricardo", apellidos ="Buendía")
    
#    return HttpResponse(layout+"""
#        <h1>Pagina de mi web</h1>
#        <h3>Creado por Eric Márquez Salas</h3>
#    """)


def pagina(request, redirigir = 0):
    
    if redirigir ==1:
        #return redirect('/contacto/')
        #return redirect('/contacto/Juan/Rivera')
        return redirect('Contacto', nombre = "Ricardo", apellidos ="Buendía")
    
    return render(request, 'pagina.html', {'texto': 'Ingeniero en Desarrollo de Software' ,
    'lenguajes': ['Python', 'JavaScript', 'HTML','CSS']})


def contacto(resquest,nombre="",apellidos=""):
    
    html =""

    if nombre and apellidos:
        html +="El nombre de nuestro experto es: "
        html += f"<h3>{nombre} {apellidos}</h3>"
    
    return HttpResponse(layout+f"""
        <h2>Experto en web</h2>
    """+html)


def crear_articulo(request, title, content, public):  #Con envío de parametros title, content, public
    
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title} - {articulo.content}</strong>")

#  ---------------------------Trabajar con formularios Django-------------------------------------------

def guardar_articulo(request):  #Con envío de parametros title, content, public, ***Ojo  También lo usaremos para trabajar con el formulario crea_articulo.html
    #  Para usar este método con el formulario debemos de preguntar si los datos viene por el método GET    
    
    if request.method == 'POST':

        title = request.POST['title']

        if len(title) <= 1:
            return HttpResponse("<h2>El título es demasiado pequeño, favor de verificar</h2>")

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
        title = title,
        content = content,
        public = public
        )
    
        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title} - {articulo.content}</strong>")
    else:

        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

    
    """
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()
    
    return HttpResponse(f"Articulo creado: <strong>{articulo.title} - {articulo.content}</strong>")
    """

def crea_articulo(request):

    return render(request, 'crea_articulo.html')

def crea_articulo_completo(request):

    if request.method == 'POST':
        
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form=formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )
    
            articulo.save()

            #  Crear mensaje flash, que se mostrará una sola vez

            messages.success(request, f'Has creado correctamente el Artículo {articulo.id}' )

            return redirect('listar-articulos')
            #return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
    else:

        formulario = FormArticle()

    return render(request, 'crea_articulo_completo.html', {
        'form' : formulario
    })

#  --------------------------------------------------------------------------------------------------

def mostrar_articulo(request):
    
    try:
        # se crea una variable para hacer uso del modelo Article en conjunto con .objects y con el método get
        # se construye una instrucción SQL
        articulo = Article.objects.get(title = "Superman", public=False)
        response=f"Articulo: <br/> {articulo.id} . {articulo.title}"
    except:
        response ="<h2>Artículo NO encontrado</h2>"
    
    return HttpResponse(response)


def editar_articulo(request, id):
    
    articulo = Article.objects.get(pk=id)

    articulo.title="The Lord of the Rings"
    articulo.content ="Película del 2001"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} actualizado: <strong>{articulo.title} - {articulo.content}</strong>")


def listar_articulos(request):
    
    lista_articulos = Article.objects.all() .order_by('-id')  #  Para listar todos los elementos
    #lista_articulos = Article.objects.order_by('id')[:4]  #  Para listar solo 4 elementos (limit)
    #lista_articulos = Article.objects.order_by('id')[2:6]  #  Para listar un rango del 2 al 6 (limit)
    #lista_articulos = Article.objects.filter(title="Jason Bourne", id=5)  #  Filtrado por criterio de algún campo
    #lista_articulos = Article.objects.filter(title__contains="The")  #  Filtrado por criterio tipo LIKE
    #lista_articulos = Article.objects.filter(title__exact="Jason Bourne")  #  Filtrado por criterio exacto
    #lista_articulos = Article.objects.filter(title__iexact="The Lord of the Rings")  #  Filtrado no importando que inicia con mayúscula o minúscula
    #lista_articulos = Article.objects.filter(id__gt=6)  #  Filtrado por criterio gt greater than
    #lista_articulos = Article.objects.filter(id__lt=6)  #  Filtrado por criterio lt less than
    #lista_articulos = Article.objects.filter(id__lte=6)  #  Filtrado por criterio lt less than o equal
    #lista_articulos = Article.objects.filter(id__lte=6, title__contains="Jason Bourne")  #  Filtrado por criterio lt less than o equal con varias condiciones 
    #lista_articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE  title = 'The Matrix Revolution' AND public=0 ")  #  Filtrado por criterio lt less than
    #lista_articulos = Article.objects.filter(
    #    Q(title__contains="Matrix") | Q(title__contains="Empire")
    #)

    return render(request, 'listar-articulos.html', {
        'lista_articulos': lista_articulos
    })


def borrar_articulo(request,id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('listar-articulos')
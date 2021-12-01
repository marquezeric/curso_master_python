from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator  #  Para utilizar la paginación
from blog.models import Category, Article  #  Para realizar consulta a los datos de estos modelos
from django.contrib.auth.decorators import login_required  #  Para requerir que se logueen los usuarios si quieren ver



# Create your views here.

@login_required(login_url="login")
def list(request):

    #  Para mostrar todos los registros que contenga Article
    articles = Article.objects.all()
    #  Paginar todos los articulos mostrados
    paginator= Paginator(articles,2)

    #  Recoger el número de paginas a mostrar
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)


    return render(request,'articles/list.html', {
        'title' : 'Artículos',
        #'articles' : articles,
        'articles' : page_articles,  #  Cuando se utiliza el paginador 
    })
@login_required(login_url="login")
def categorie(request,category_id):

    category = get_object_or_404(Category, id=category_id)
    #articles = Article.objects.filter(categories=category_id)  #  También se puede omitir

    return render(request,'categories/category.html',{
        'category':category,
        #'articles':articles,# Se puede omitir en conjunto con la instrucción que esta en Category.html include
    })
@login_required(login_url="login")
def article(request,article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
            'article':article,
        })

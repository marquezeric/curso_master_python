from django.db.models.expressions import OrderBy
from blog.models import Category, Article

#  Subsonsultas con DJango
#  Solo se visualizarán aquellas categorías que se estén usando

def get_categories(request):

    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    return {
        'categories':categories,
        'ids':categories_in_use
    }
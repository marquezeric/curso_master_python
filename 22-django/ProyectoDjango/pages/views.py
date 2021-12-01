from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required  #  importamos funciones para requerir login en caso 

# Create your views here.
@login_required(login_url="login")
def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page": page
    })

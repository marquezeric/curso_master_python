from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Signup(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = NameForm()
    #option1
    """
    template = loader.get_template('signup.html')
    context= {
        'form': form,
    }
    return HttpResponse(template.render(context,request))
    """
    return render(request, 'signup.html', {'form': form})
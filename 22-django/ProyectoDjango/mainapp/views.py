from django.shortcuts import render
from django.shortcuts import redirect  #  Para cuando se logueen los redireccione a una página en específico
from django.contrib.auth.forms import UserCreationForm # formulario que tiene Django
from mainapp.forms import RegisterForm  #  Importamos el Objeto RegisterForm que se encuentra en forms.py 
from django.contrib import messages  #  Importación para el uso Mensajes que duran una actualización de pantalla
from django.contrib.auth import authenticate, login, logout  #  Importación del modulo de autenticación



# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title' : 'Inicio'
    })

def about(request):

    return render(request, 'mainapp/about.html', {
        'title' : 'Acerca de mi'
    })

def register_page(request):
#  No muestre las opciones de registro, login cuando se este logueado
    if request.user.is_authenticated:

        return redirect('inicio')
    else:

        #register_form = UserCreationForm()  #  Uso del formulario por Defaul que tiene Django
        register_form = RegisterForm()  #  Uso del formulario personalizado en base a un modelo de nuestra tabla auth_user

        if request.method == 'POST':
            #register_form = UserCreationForm(request.POST)  #  Uso del formulario por Defaul que tiene Django
            register_form = RegisterForm(request.POST)  #  Uso del formulario personalizado

            if register_form.is_valid():
                register_form.save()
                #  Uso del mensaje flash que solo durará hasta que se actualice la pantalla
                messages.success(request, "Te has registrado correctamente")
                
                return redirect('inicio')

        return render(request, 'users/register.html', {
            'title': 'Registro',    # Título que deseemos que se visualce
            'register_form':  register_form
        })

# Generación de la pagina Login Page

def login_page(request):

    if request.user.is_authenticated:

        return redirect('inicio')
    else:
#  Lógica de autenticación solo 4 funciones
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

    #   Creamos un objeto usuario con la variable user para usar la función authenticate
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('inicio')
            else:
                messages.warning(request, 'No te registraste correctamente')

        
        return render(request,'users/login.html', {
            'title': 'Login'
        })
#   Creamos la función para cerrar la sesión de usuario logueado
def logout_user(request):
    logout(request)
    
    return redirect('login')

#  Creación de un formulario personalizado
#  Basado en un modelo

from django import forms
from django.core import validators

#  Basado en el formulario que maneja Django pero con nuestro custom
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

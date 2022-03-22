from dataclasses import fields
from django.forms import ModelForm
from .models import Order, Customer
from django.contrib.auth.forms import UserCreationForm #  Móldulo para el login y register
from django.contrib.auth.models import User  #  Móldulo para el login y register
from django import forms
#  Creación de un Form con Python

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
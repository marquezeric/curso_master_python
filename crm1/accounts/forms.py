from dataclasses import fields
from django.forms import ModelForm
from .models import Order
#  Creación de un Form con Python
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
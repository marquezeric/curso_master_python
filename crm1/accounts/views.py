from http.client import HTTPResponse
#from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Customer, Order, Product  #  Importamos nuestros modelos que deseamos trabajar

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()  #  Presenta total

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context={'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})
    #return HttpResponse('products')

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()

    context = {'customer': customer, 'orders': orders}
    return render(request, 'accounts/customer.html')
    #return HttpResponse('customer')


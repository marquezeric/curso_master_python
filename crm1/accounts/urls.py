from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('updateOrder/<str:pk>/', views.updateOrder, name="update_order"),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('createCustomer/', views.createCustomer, name="create_customer"),

    #path('frecuencias/edit/<int:pk>/',editfrecuencia.as_view(), name='edit_frec'),

]
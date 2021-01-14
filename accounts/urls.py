from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/<str:customer_id>', views.customers, name='customer'),
    path('create-order', views.create_order, name='create_order'),
    path('update-order/<str:order_id>', views.update_order, name='update_order'),
    path('delete-order/<str:order_id>', views.delete_order, name='delete_order'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customers/<str:customer_id>', views.customers, name='customers'),
]

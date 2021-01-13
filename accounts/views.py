from django.shortcuts import render
from accounts.models import *


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    total_pending_orders = orders.filter(status='Pending').count()
    total_delivered_orders = orders.filter(status='Delivered').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'total_pending_orders': total_pending_orders,
        'total_delivered_orders': total_delivered_orders,
    }

    return render(request, 'pages/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})

def customers(request):
    return render(request, 'pages/customers.html')

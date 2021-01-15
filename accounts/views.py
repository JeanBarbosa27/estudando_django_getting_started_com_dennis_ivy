from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from accounts.models import *
from accounts.forms import OrderForm


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    total_pending_orders = orders.filter(status='Pending').count()
    total_delivered_orders = orders.filter(status='Delivered').count()

    context = {
        'customers': customers,
        'orders': orders.order_by('-date_created')[:5],
        'total_orders': total_orders,
        'total_pending_orders': total_pending_orders,
        'total_delivered_orders': total_delivered_orders,
    }

    return render(request, 'pages/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})

def customers(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
    }

    return render(request, 'pages/customers.html', context)

def create_order(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=10
    )
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('dashboard')

    context = {'formset': formset, 'title': 'Create New Order'}
    return render(request, 'pages/order_form.html', context)

def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'title': f"Update Order {order}"
    }

    return render(request, 'pages/order_form.html', context)

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')

    return render(request, 'pages/delete_order.html', {'order': order})

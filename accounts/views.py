from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import *
from accounts.forms import OrderForm, CreateUserForm
from accounts.filters import OrderFilter
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']

            message = f"Account was created for {username}."
            messages.success(request, message)

            return redirect('login')

    return render(request, 'pages/register.html', {'form': form})

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect!')


    return render(request, 'pages/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')

def user_page(request):
    return render(request, 'pages/user.html')

@login_required(login_url='login')
@admin_only
def dashboard(request):
    print('entrou no método')
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


@login_required(login_url='login')
@admin_only
def products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})


@login_required(login_url='login')
@admin_only
def customers(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    total_orders = orders.count()

    filter_orders = OrderFilter(request.GET, queryset=orders)
    orders = filter_orders.qs

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'filter_orders': filter_orders.form,
    }

    return render(request, 'pages/customers.html', context)


@login_required(login_url='login')
@admin_only
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


@login_required(login_url='login')
@admin_only
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


@login_required(login_url='login')
@admin_only
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    return render(request, 'pages/delete_order.html', {'order': order})

from django.shortcuts import render

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def products(request):
    return render(request, 'pages/products.html')

def customers(request):
    return render(request, 'pages/customers.html')

from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_only
from accounts.models import Product


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(admin_only, name='dispatch')
class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'pages/products.html', {'products': products})

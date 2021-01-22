from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_only
from accounts.models import Customer
from accounts.filters import OrderFilter


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(admin_only, name='dispatch')
class CustomersView(View):
    def get(self, request, customer_id):
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

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.models import *
from accounts.decorators import admin_only


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(admin_only, name='dispatch')
class DashboardView(View):
    def get(self, request):
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

from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_only
from accounts.models import Order
from accounts.forms import OrderForm


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(admin_only, name='dispatch')
class UpdateOrderView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        form = OrderForm(instance=order)
        context = {
            'form': form,
            'title': f"Update Order {order}"
        }

        return render(request, 'pages/order_form.html', context)

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    # context = {
    #     'form': form,
    #     'title': f"Update Order {order}"
    # }

    # return render(request, 'pages/order_form.html', context)

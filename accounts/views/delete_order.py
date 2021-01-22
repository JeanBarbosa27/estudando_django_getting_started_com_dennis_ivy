from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_only
from accounts.models import Order


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(admin_only, name='dispatch')
class DeleteOrderView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)

        return render(request, 'pages/delete_order.html', {'order': order})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)

        if request.method == 'POST':
            order.delete()
            return redirect('dashboard')

from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

from accounts.decorators import admin_only
from accounts.models import Customer, Order


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(admin_only, name='dispatch')
class CreateOrderView(View):
    def __init__(self):
        self.context = {'title': 'Create New Order'}
        self.OrderFormSet = inlineformset_factory(
            Customer, Order, fields=('product', 'status'), extra=10
        )

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        self.context['formset'] = self.OrderFormSet(queryset=Order.objects.none(), instance=customer)

        return render(request, 'pages/order_form.html', self.context)

    def post(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        formset = self.OrderFormSet(request.POST, instance=customer)
        self.context['formset'] = formset

        if formset.is_valid():
            formset.save()
            return redirect('dashboard')

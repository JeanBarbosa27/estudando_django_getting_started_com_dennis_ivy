from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_users


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['customer']), name='dispatch')
class UserPageView(View):
    def get(self, request):
        orders = request.user.customer.order_set.all()
        total_orders = orders.count()
        total_pending_orders = orders.filter(status='Pending').count()
        total_delivered_orders = orders.filter(status='Delivered').count()

        context = {
            'orders': orders,
            'total_orders': total_orders,
            'total_pending_orders': total_pending_orders,
            'total_delivered_orders': total_delivered_orders,
        }

        return render(request, 'pages/user.html', context)

from django.contrib import admin

from accounts.models import *
from .customer import CustomerAdmin
from .orders import OrderAdmin
from .products import ProductAdmin

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)

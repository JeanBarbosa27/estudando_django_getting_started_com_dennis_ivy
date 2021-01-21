from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'customer',
        'product',
        'notes',
        'date_created',
    )

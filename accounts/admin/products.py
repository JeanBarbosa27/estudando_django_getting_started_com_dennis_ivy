from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'category',
        'description',
        'date_created',
    )

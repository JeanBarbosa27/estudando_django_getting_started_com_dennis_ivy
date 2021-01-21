from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'phone',
        'email',
        'date_created',
    )

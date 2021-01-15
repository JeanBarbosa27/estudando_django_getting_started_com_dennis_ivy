from django_filters import FilterSet, DateFilter, CharFilter

from accounts.models import *


class OrderFilter(FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')

    class Meta:
        model = Order
        exclude = ['customer', 'date_created']

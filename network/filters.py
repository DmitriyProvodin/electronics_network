import django_filters
from .models import NetworkNode


class NetworkNodeFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = NetworkNode
        fields = ['country']

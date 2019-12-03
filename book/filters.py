from .models import Book
import django_filters

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    year_published = django_filters.NumberFilter(name='date_joined', lookup_expr='year_published')
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year_published']
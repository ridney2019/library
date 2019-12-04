from django.shortcuts import render
from django.db.models import Q
from django.views.generic import (CreateView, ListView, UpdateView,TemplateView )
from .models import Author, Book, Genre
from .forms import AuthorForm, BookForm, GenreForm, SearchForm
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    model = Book
    template_name = 'book/welcome.html'
    success_url = ("book:base")


class AuthorView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author_create.html'
    success_url = reverse_lazy("book:author_create")

    def get_context_data(self):
        context = super().get_context_data()
        context['author_list'] = self.model.objects.all()
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'book/author_create.html'
    success_url = ("book:author_update")
    form_class = AuthorForm


class BookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = reverse_lazy("book:book_view")

def get_context_data(self):
    context = super().get_context_data()
    context['book_list'] = self.model.objects.all()
    return context


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = ("book:book_update") 


class GenreView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'book/genre_create.html'
    success_url = reverse_lazy("book:genre_create")

    def get_context_data(self):
        context = super().get_context_data()
        context['genre_list'] = self.model.objects.all()
        return context

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'book/genre_create.html'
    success_url = ("book:genre_update")


class SearchResultsView(ListView):
    model = Book
    template_name = 'book/search.html'
    success_url = ("book:search_view")
    form_class = SearchForm
    
def get_queryset(self):
        queryset = super().get_queryset()
        to_query = self.request.GET.get('q', None) or self.request.POST.get('q', None)
        q = Q()
        if to_query:
            q = Q(title__icontains=to_query) | Q(author__icontains=to_query) | Q(year_published__icontains=to_query) | Q(genre__icontains=to_query)
            queryset = queryset.filter(q)
         
        return queryset
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

    def Autores(self):
        return Author.objects.all()


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'book/author_create.html'
    success_url = ("book:author_update")
    fields = '__all__'


class BookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = reverse_lazy("book:book_view")

    def Livros(self):
        return Book.objects.all()


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

    def Generos(self):
        return Genre.objects.all()

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'my-book-edit.html'
    success_url = ("book:genre_update")


class SearchResultsView(ListView):
    model = Book
    template_name = 'book/search.html'
    success_url = ("book:search_view")
    paginate_by = 30 
    form_class = SearchForm

def get_queryset(self):
        query = self.request.GET.get('q')

        results = Book.objects.filter
        (
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return results
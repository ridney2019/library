from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from .filters import BookFilter
from .views import  HomePageView, AuthorView, AuthorUpdateView, BookView, BookUpdateView, GenreView, GenreUpdateView, SearchResultsView

app_name='book'

urlpatterns = [
    #HomePage
    path( 'welcome/', HomePageView.as_view(), name='base'),

    #Author
    path('author_create/', AuthorView.as_view(), name='author_create'),
    path('author_create/', AuthorUpdateView.as_view(), name='author_update'),

    #Book
    path('book_create/', BookView.as_view(), name='book_view'),
    path('book_create/', BookUpdateView.as_view(), name='book_update'), 
    path('search/', SearchResultsView.as_view(), name='search_results'),

    #Genre
    path('genre_create/', GenreView.as_view(), name='genre_create'),
    path('genre_create/', GenreUpdateView.as_view(), name='genre_update'),
]
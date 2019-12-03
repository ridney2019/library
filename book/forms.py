from django.forms import ModelForm
from .models import Author, Book, Genre
from django import forms

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_time', 'date_time_modification']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [ 'author', 'title', 'genre', 'languange', 'pages', 'code', 'year_published', 'date_time', 'date_time_modification']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['description', 'date_time', 'date_time_modification' ]

'''class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)'''

class SearchForm(forms.Form):
    search_title =  forms.CharField(
                    required = False,
                    label='Título!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    search_genre = forms.CharField(
                    required = False,
                    label='Search age (exact match)!'
                  )


from django.contrib import admin
from .models import Author, Book, Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'date_time','date_time_modification']
    search_fields = ['user__first_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author','date_time','date_time_modification']
    readonly_fields = ['date_time','date_time_modification']
    search_fields = ['title', 'author',]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ['description']
    search_fields = ['description']



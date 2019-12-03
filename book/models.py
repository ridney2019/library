from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(verbose_name='Nome', max_length=20)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=20)
    date_time = models.DateTimeField(verbose_name='Criado em', null=True , blank=True)
    date_time_modification = models.DateTimeField(verbose_name='Atualizado em:', null=True , blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
   
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
       return self.first_name


class Book(models.Model):
    author = models.ForeignKey(Author,verbose_name='Autor', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Título', max_length=40)
    genre = models.CharField(verbose_name='Gênero', max_length=20)
    languange = models.CharField(verbose_name='Idioma', max_length=10)
    pages = models.IntegerField(verbose_name='Páginas')
    code = models.IntegerField(verbose_name='Código')
    year_published = models.IntegerField(verbose_name='Ano Publicação')
    date_time = models.DateTimeField(verbose_name='Criado em', null=True , blank=True )
    date_time_modification = models.DateTimeField(verbose_name='Atualizado em', null=True , blank=True )

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.title


class Genre(models.Model):
    description = models.CharField(verbose_name='Descrição', max_length=250)
    date_time = models.DateTimeField(verbose_name='Criado em', null=True , blank=True  )
    date_time_modification = models.DateTimeField(verbose_name='Atualizado em', null=True , blank=True )

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.description
from django.db import models
from registration.models import UsersBook
# Create your models here.



class Books(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название книги')
    autors = models.ForeignKey('Autor', on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name="Жанр")
    description = models.TextField(max_length=500, verbose_name='Описание', blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книгу"

class Categories(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название жанра')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = "Жанр"


class Autor(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя автора')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия автора')
    def __str__(self):
        name = self.first_name
        second = self.second_name
        return f"{name} {second}"

    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"
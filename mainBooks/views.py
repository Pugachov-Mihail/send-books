import os

from django.shortcuts import render, redirect

from books import settings
from .models import Autor, Books, Categories
from registration.form import CreateUser
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import BooksForm, AutorForm, CategoriesForms
from django.http import HttpResponse, Http404


# Create your views here.


def index(requests):
    #Вывод данных из модели books на главной страницы
    books = Books.objects.all()
    categor = Categories.objects.all()
    template = 'mainBook/index.html'
    contex = {
        'books': books,
        'categiries': categor
              }
    return render(requests, template, contex)


def office(request):
    #Личный кабинет и выгрузка книг
    book = Books.objects.all()
    template = 'mainBook/office.html'
    content = {
        'books': book,
    }
    return render(request, template, content)

def download(request, path):
    #Загрузка файлов
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminpuload")
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response
    raise Http404

def createAvtor(request):
    #Создание автора
    template = 'mainBook/createAvtor.html'
    if request.method == 'POST':
        autor = AutorForm(request.POST)
        if autor.is_valid():
            autor.save()
            return redirect('createCateg')
    else:
        autor = AutorForm()
    context = {
       'autors': autor,
    }
    return render(request, template, context)

def createCategories(request):
    #создание жанров книг
    template = 'mainBook/createCategories.html'
    if request.method == 'POST':
        categories = CategoriesForms(request.POST)
        if categories.is_valid():
            categories.save()
            return redirect('createBooks')
    else:
        categories = CategoriesForms()
    context = {
        'categories': categories,
    }
    return render(request, template, context)

def createBooks(request):
    #загрузка самих книг
    template = 'mainBook/createBooks.html'
    if request.method == 'POST':
        books = BooksForm(request.POST, request.FILES)
        if books.is_valid():
            books.save()
            return redirect('office')
    else:
        books = BooksForm()
    context = {
        'form': books,
    }
    return render(request, template, context)

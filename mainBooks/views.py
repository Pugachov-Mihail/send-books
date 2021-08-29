from django.shortcuts import render, redirect
from .models import Autor, Books, Categories
from registration.form import CreateUser
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import BooksForm, AutorForm, CategoriesForms
# Create your views here.


def index(requests):
    books = Books.objects.all()
    categor = Categories.objects.all()
    template = 'mainBook/index.html'
    contex = {
        'books': books,
        'categiries': categor
              }
    return render(requests, template, contex)


def office(request):
    book = Books.objects.all()
    template = 'mainBook/office.html'
    content = {
        'books': book,
    }
    return render(request, template, content)

def createAvtor(request):
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
    template = 'mainBook/createBooks.html'
    if request.method == 'POST':
        books = BooksForm(request.POST)
        if books.is_valid():
            books.save()
            return redirect('office')
    else:
        books = BooksForm()
    context = {
        'form': books,
    }
    return render(request, template, context)

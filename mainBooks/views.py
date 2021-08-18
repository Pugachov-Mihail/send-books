from django.shortcuts import render
from .models import Autor, Books, Categories
from registration.form import CreateUser
from django.contrib.auth.models import User
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
    user = User.objects.all()
    template = 'mainBook/office.html'
    content = {
        'users': user,
    }
    return render(request, template, content)
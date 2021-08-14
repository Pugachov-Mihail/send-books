from django.shortcuts import render
from .models import Autor, Books, Categories
from registration.form import Login, CreateUser
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

def registration(requests):
    form = CreateUser
    template = 'mainBook/registaration/regist.html'
    context = {'form': form }
    return render(requests, template, context)
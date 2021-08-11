from django.shortcuts import render
from .models import Autor, Books, Categories

# Create your views here.


def index(requests):
    books = Books.objects.all()
    template = 'mainBook/index.html'
    contex = {'books': books}
    return render(requests,template, contex)

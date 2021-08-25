from django.shortcuts import render, redirect
from .models import Autor, Books, Categories
from registration.form import CreateUser
from django.contrib.auth.models import User
from registration.models import UsersBook
from .forms import BooksForm
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

def download(request):
    template = 'mainBook/download.html'
    if request.method=="POST":
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mainBooks:index')
        else:
            form = BooksForm()
    context = {'form': form}
    return render(request, template, context)
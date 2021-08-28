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
        'users': book,
    }
    return render(request, template, content)

def createView(request):
    template = 'mainBook/download.html'
    autor = AutorForm
    book = BooksForm
    categories = CategoriesForms
    context = {
        'autors': autor,
        'form': book,
        'categories': categories
    }
    if request.method == 'POST':
        autor = AutorForm(request.POST)
        if autor.is_valid():
            autor.save()
    else:
        autor = AutorForm()
    return render(request, template, context)


'''class BooksCreateView(CreateView):
    template_name = 'mainBook/download.html'
    form_class = BooksForm
    success_url = reverse_lazy('office')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autors'] = AutorForm
        context['categories'] = CategoriesForms
        return context'''
from django.shortcuts import render

# Create your views here.


def index(requests):
    contex = {'hello':'Привет Андрей!'}
    return render(requests,'mainBook/index.html', contex)

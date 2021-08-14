from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class Login(CreateView):
    form_class = LoginView
    template_name = 'mainBook/registaration/login.html'


class CreateUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'mainBook/registaration/regist.html'

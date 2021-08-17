from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = 'mainBook/registration/login.html'
    success_url = 'index/'



class CreateUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'mainBook/registration/regist.html'

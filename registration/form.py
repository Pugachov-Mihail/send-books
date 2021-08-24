from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django import forms

class UserRegistForms(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(LoginView):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class Login(LoginView):
    template_name = 'mainBook/registration/login.html'
    success_url = reverse_lazy('office')



class CreateUser(CreateView):
    form_class = UserRegistForms
    success_url = reverse_lazy('index')
    template_name = 'mainBook/registration/regist.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(reverse('office'))


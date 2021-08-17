from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = 'mainBook/registration/login.html'
    success_url = 'index/'



class CreateUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'mainBook/registration/regist.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        logins = super(CreateUser, self).form_valid(form)
        return logins

    #allods95

from django.urls import path
from .views import index, office, BooksCreateView
from django.contrib.auth.views import LoginView, LogoutView
from registration.form import Login, CreateUser
from django.contrib.auth.models import User



urlpatterns = [
    path('', index, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', CreateUser.as_view(), name='registration'),
    path('office/', office, name='office'),
    path('download/', BooksCreateView.as_view(), name='download')
]
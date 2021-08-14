from django.urls import path
from .views import index, registration
from registration.form import Login


urlpatterns = [
    path('', index, name='index'),
    path('accaunts/login', Login.as_view(), name='login'),
    path('registration/', registration, name='registration'),
]
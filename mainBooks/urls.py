from django.urls import path
from .views import index, office, createAvtor, createCategories, createBooks, api_index
from django.contrib.auth.views import LoginView, LogoutView
from registration.form import Login, CreateUser
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

from django.contrib.auth.models import User



urlpatterns = [
    path('', index, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', CreateUser.as_view(), name='registration'),
    path('office/', office, name='office'),
    path('office/createAvtor/', createAvtor, name='createAvtor'),
    path('office/createCategories/', createCategories, name='createCateg'),
    path('office/createBooks/', createBooks, name='createBooks'),
    path(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('api/', api_index),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

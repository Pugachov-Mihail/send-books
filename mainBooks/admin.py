from django.contrib import admin
from .models import Autor, Categories, Books
from registration.models import UsersBook
# Register your models here.

admin.site.register(UsersBook)
admin.site.register(Categories)
admin.site.register(Autor)
admin.site.register(Books)


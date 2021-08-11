from django.contrib import admin
from .models import Autor, Categories, Books
# Register your models here.

admin.site.register(Books)
admin.site.register(Categories)
admin.site.register(Autor)
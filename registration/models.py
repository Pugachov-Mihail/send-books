from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsersBook(models.Model):
    books = models.ForeignKey('mainBooks.Books', on_delete=models.CASCADE)
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)


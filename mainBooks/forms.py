from django import forms
from django.core.validators import FileExtensionValidator
from .models import Books

class BooksForm(forms.ModelForm):
    book = forms.FileField(label='Загрузите книгу', validators=[
        FileExtensionValidator(allowed_extensions=('pdf', 'fb2', 'mobi', 'epab', 'djvu'))
    ],error_messages={'invalid_extension': 'Этот формат не поддерживается'})
    name = forms.CharField(label='Название книги', max_length=50,widget=forms.TextInput())
    autors = forms.CharField(label='Автор', max_length=40,widget=forms.TextInput())
    categories = forms.CharField(label='Жанр',widget=forms.TextInput(),max_length=20)
    description = forms.CharField(label='Описание',empty_value=True ,widget=forms.TextInput())
    class Meta:
        model = Books
        fields = '__all__'
from django import forms
from django.core.validators import FileExtensionValidator
from .models import Books, Autor, Categories

class AutorForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя автора',max_length=20,widget=forms.TextInput())
    second_name = forms.CharField(label='Фамилия автора',max_length=20, widget=forms.TextInput())
    class Meta:
        model = Autor
        fields = '__all__'


class CategoriesForms(forms.ModelForm):
    title = forms.CharField(label="Жанр" ,max_length=20, widget=forms.TextInput())

    class Meta:
        model = Categories
        fields = '__all__'



class BooksForm(forms.ModelForm):
    book = forms.FileField(label='Загрузите книгу', validators=[
        FileExtensionValidator(allowed_extensions=('pdf', 'fb2', 'mobi', 'epab', 'djvu'))
    ],error_messages={'invalid_extension': 'Этот формат не поддерживается'}, widget=forms.FileInput())
    name = forms.CharField(label='Название книги', max_length=50,widget=forms.TextInput())
    description = forms.CharField(label='Описание', empty_value=True ,widget=forms.TextInput(), required=False)

    class Meta:
        model = Books
        fields = ('name', 'description','book',)


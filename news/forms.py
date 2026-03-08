from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of article'}),
            'anons': TextInput(attrs={'class': 'form-control', 'placeholder': 'Anons of article'}),
            'full_text': Textarea(attrs={'id': 'article', 'class': 'form-control', 'placeholder': 'Text of article'}),
            'date': DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control', 'placeholder': 'Date of article'})
        }
from django import forms
from .models import *


class LibroForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = (
            'usuario',
            'img',
            'titulo',
            'categoria',
            'descripcion',
            'autor',
            'pdf'
        )
        exclude = ['usuario']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
class HistoryForm(forms.ModelForm):
    class Meta:
        model = HistoryModel
        fields = (
            'usuario',
            'img',
            'titulo',
            'categoria',
            'descripcion',
            'autor',
            'text',
        )

        exclude = ['usuario']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),

            
        }

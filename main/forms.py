from django import forms
from django.core.exceptions import ValidationError
from .models import Films , Director

class FilmFrom(forms.ModelForm):
    class Meta:
        model = Films
        fields = '__all__'
        widgets = {
            'director': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Films.objects.filter(title=title).count() > 0:
            raise ValidationError('Yo man, we already have this film')
        return title


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(title=name).count() > 0:
            raise ValidationError('Yo man , we already have this director')
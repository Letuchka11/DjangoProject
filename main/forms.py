from django import forms
from django.core.exceptions import ValidationError
from .models import Films , Director
from django.contrib.auth.models import User

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

class UserCreateForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError('This username is already exists maan!')

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError('Passwords should be same !')
        return password1


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


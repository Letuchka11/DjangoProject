from django.shortcuts import render , Http404 , redirect
from datetime import datetime
from .models import Films , Director
from .forms import DirectorForm , FilmFrom ,UserCreateForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

def log_out_view(request):
    logout(request)
    return redirect('/main/')

def login_view(request):
    context = {
        'form': UserLoginForm,
        'films': Films.objects.all()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/main/')

    return render(request, 'login.html', context=context)
def register_view(request):
    context = {
        "form" : UserCreateForm(),
        'films': Films.objects.all()

    }
    if request.method == "POST":
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')
        context['form'] = form
    return render(request, 'register.html', context=context)

# Create your views here.



def create_director_view(request):
    context = {
        'films' : Films.objects.all(),
        'forms' : DirectorForm
    }
    if request.method == 'GET':
        context['form'] = DirectorForm()
        return render(request, 'create_director.html', context)
    else:
        form = DirectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')



def create_film_view(request):
    context = {
        'films' : Films.objects.all(),
        'forms' : FilmFrom
    }
    if request.method == 'GET':
        context['form'] = FilmFrom()
        return render(request, 'create_film.html', context)
    else:
        form = FilmFrom(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')


def index_view(request):
    print(request.user)
    context={
        'director': Director.objects.all()
    }

    return render(request, 'index.html' , context=context)

def director_view(request, director_id):
    try:
        directors = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404("Director not found")
    director_dict={
        "director" : directors,
        "directors": Director.objects.all()
    }
    return render(request, "director.html", context=director_dict)

def about_us(request):
    return render(request, 'about_us.html')

def date_now(request):
    date = datetime.now()
    context = {
        "year" : date.year,
        "month" : date.month,
        "day" : date.day,
        "hour" : date.hour,
        "seconds" : date.second
    }
    return render(request, 'date_now.html', context=context)

def films_list_view(request):
    context = {
        "films" : Films.objects.all(),
        "directors": Director.objects.all()
    }
    return render(request, "films.html", context=context)

def films_id_view(request, id):
    context = {}
    try:
        film = Films.objects.get(id=id)
    except Films.DoesNotExist:
        raise Http404("Films not found")
    context['film_id'] = film
    return render(request, 'film_id_list.html', context=context)
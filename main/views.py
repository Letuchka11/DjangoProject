from django.shortcuts import render , Http404
from datetime import datetime
from .models import Films , Director

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

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
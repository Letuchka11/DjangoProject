from django.shortcuts import render
from datetime import datetime
from .models import Films

# Create your views here.
def index_view(request):
    return render(request , 'index.html')

def about_us(request):
    return render(request , 'about_us.html')

def date_now(request):
    date = datetime.now()
    context = {
        "year" : date.year,
        "month" : date.month,
        "day" : date.day,
        "hour" : date.hour,
        "seconds" : date.second
    }
    return render(request, 'date_now.html' , context=context)

def films_list_view(request):
    context = {
        "films" : Films.objects.all()
    }
    return render(request , "films.html" , context=context)

def films_id_view(request, id):
    context = {}
    film = Films.objects.get(id=id)
    context['film_id'] = film
    return render(request , 'film_id_list.html' , context=context)
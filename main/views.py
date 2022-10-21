from django.shortcuts import render
from datetime import datetime

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
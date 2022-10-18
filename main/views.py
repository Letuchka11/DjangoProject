from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request , 'index.html')

def about_us(request):
    return render(request , 'about_us.html')

def date_now(request):
    return render(request, 'date_now.html')
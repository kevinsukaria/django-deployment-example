from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, Accessrecord


# Create your views here.
def index(request):
    my_dict = {
        'insert_me': 'Hello I am from views.py'
    }

    webpages_list = Accessrecord.objects.order_by('date')

    date_dict = {
        'access_dates': webpages_list
    }
    return render(request, 'first_app/index.html', context=date_dict)

def homepage(request):
    return render(request, 'first_app/homepage.html')
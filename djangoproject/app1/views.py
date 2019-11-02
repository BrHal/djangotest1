from django.shortcuts import render
from datetime import datetime


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html', {"now": datetime.now()})

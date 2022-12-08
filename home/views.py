
from django.shortcuts import render
from django.http import HttpResponse

from .models import Information

# Create your views here.
def home(request):
    info=Information.objects.all()
    return render(request,'home.html',{'info' : info})

 
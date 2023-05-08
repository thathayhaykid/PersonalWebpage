from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'hello.html', {'name' : 'Haythem'})
    #return render(request, 'hello.html', {'name' : 'Haythem'})

def heytala(request):
    return render(request,'HeyTala.html')

# Create your views here.

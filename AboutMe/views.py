from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x=1
    x=2
    return render(request, 'hello.html', {'name' : 'Haythem'})
    #return render(request, 'hello.html', {'name' : 'Haythem'})


# Create your views here.

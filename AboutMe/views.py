from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'hello.html', {'name' : 'Haythem'})
    #return render(request, 'hello.html', {'name' : 'Haythem'})


# Create your views here.

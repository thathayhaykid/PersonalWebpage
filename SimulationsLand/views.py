from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'SlidingCar.html', {'name' : 'Hey There we are putting simulations here soon idc where tho'})

#return render(request, 'hello.html', {'name' : 'Haythem'})

# Create your views here.

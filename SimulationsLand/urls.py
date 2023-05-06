from django.urls import path

from . import views

#URLConfModule
urlpatterns = [
    path('slidingcar/', views.say_hello)
]
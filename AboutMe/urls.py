from django.urls import path

from . import views

#URLConfModule
urlpatterns = [
    path('hello/', views.say_hello),
    path('HeyTala/', views.heytala),
    path('home/', views.home)
]
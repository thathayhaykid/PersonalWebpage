# This file is cool

from .common import *
import dj_database_url
import os

DEBUG = False

if DEBUG is True:
    ALLOWED_HOSTS = [
    '127.0.0.1:8000'
    ]
else:
    ALLOWED_HOSTS = [
    'haymansour.herokuapp.com',
    ]

if DEBUG is True:
    SECRET_KEY = SECRET_KEY = "django-insecure-rzqpltar+2ki1f2n=4oxwranltflpzi8x#5n$u)fo6f^7q)a1r"
else:
    SECRET_KEY = os.environ['HAYWEBSITE_SECRET_KEY']

if DEBUG is True:
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "BiggerOnTheInside",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "hayhay12!" }}
else:
        DATABASES = { "default": dj_database_url.config() }

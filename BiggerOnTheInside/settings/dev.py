from .common import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rzqpltar+2ki1f2n=4oxwranltflpzi8x#5n$u)fo6f^7q)a1r"

#what the heck man

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "BiggerOnTheInside",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "MyPassword"
    }

}


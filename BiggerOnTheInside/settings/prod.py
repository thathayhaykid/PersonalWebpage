from .common import *
import dj_database_url
import os

DEBUG = False

ALLOWED_HOSTS = [
    'haymansour.herokuapp.com'
]

SECRET_KEY = os.environ['HAYWEBSITE_SECRET_KEY']

DATABASES = {
    "default": dj_database_url.config()
}

from .base import *
from .util import get_secure_data

ALLOWED_HOSTS = ["127.0.0.1"]

# Debug Options
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
db_data = get_secure_data('.secure/db.json')

if db_data['default'] == "":
    raise ImproperlyConfigured(
        "Please input db.json in .secure/")

DATABASES = db_data

# 허용할 Origin 추가
CORS_ALLOWED_ORIGINS = [
    'https://subculture-map-frontend.pages.dev',
    'http://127.0.0.1:8000'
]

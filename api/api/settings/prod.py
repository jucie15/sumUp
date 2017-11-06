from .common import *


DEBUG = False

ALLOWED_HOSTS = ['http://13.125.14.170/', '13.125.14.170']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

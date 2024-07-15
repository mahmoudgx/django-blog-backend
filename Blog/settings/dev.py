from .common import *


SECRET_KEY = 'django-insecure-1#$qoi__24$zy#u^-5^ro**9l8%b8$f#mrcv)t)ic++_i5un7e'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog2',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
import os
import dj_database_url
from .common import *


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['blog-prod-0c3f86c27938.herokuapp.com']



DATABASES = {
    'default': dj_database_url.config()
}

DATABASES['default']['OPTIONS'] = {
    'charset': 'utf8mb4',
}

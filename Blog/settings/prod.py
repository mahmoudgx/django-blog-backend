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


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
   }
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False  # Add this line to prevent file overwriting

   # Remove the AWS_DEFAULT_ACL setting

   # Static files settings
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

   # Media files settings
DEFAULT_FILE_STORAGE = 'Blog.storage_backends.MediaStorage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
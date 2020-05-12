# pylint: disable=W0614,W0401
# import sys
# from .base import *   # noqa
from .base import PROJECT_DIR

DEBUG = True
API_TYPE = 'devel'

# sys.path.insert(0, BASE_DIR)
# sys.path.insert(0, PROJECT_DIR)
# sys.path.insert(0, PROJECT_ROOT)
# print(sys.path)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mmt_backend_test',
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': 'getwork@123',  # Not used with sqlite3.
        'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306'
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s\t{%(filename)s:%(lineno)d}\t%(levelname)s\t%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': '/var/tmp/django_cache',
   },
    'default-session': {
'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': '/var/tmp/django_cache',
    }
}

STATIC_ROOT = PROJECT_DIR + '/static/'
HOST = 'http://localhost:9011'

# pylint: disable=wildcard-import,W0614
from .base import *   # noqa

DEBUG = False
API_TYPE = 'prod'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mmt_backend',
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '127.0.0.1',  # Set to empty string for localhost.
        'PORT': '3306'
    }
}

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': '/var/tmp/django_cache',
   }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(processName)s\tf%(asctime)s\t{%(filename)s:%(lineno)d}\t%(levelname)s\t'
                      '%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
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
        'level': 'INFO'
    }
}

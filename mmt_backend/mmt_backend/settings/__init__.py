__author__ = 'sumit.gupta'

import os
from .base import *

ENVIRONMENT_NAME = os.environ.setdefault('CURR_ENV', 'DEV').lower()


if ENVIRONMENT_NAME in {'dev', 'devel'}:
    from .devel import *

# elif ENVIRONMENT_NAME == 'pp':
#     from .pp import *
#
# elif ENVIRONMENT_NAME == 'prodpp':
#     from .prodpp import *

elif ENVIRONMENT_NAME == 'prod':
    from .prod import *

# elif ENVIRONMENT_NAME == 'test':
#     from .test_settings import *

else:
    raise Exception("Settings not found.")

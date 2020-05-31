"""
WSGI config for skeleton project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys


if '/opt/repositories/skeleton/' not in sys.path:
    sys.path.append('/opt/repositories/skeleton/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'skeleton.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

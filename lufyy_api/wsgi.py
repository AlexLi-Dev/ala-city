"""
WSGI config for lufyy_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# env = os.environ.get('DJANGO_ENV', 'dev')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lufyy_api.settings.dev')

application = get_wsgi_application()

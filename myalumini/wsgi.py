"""
WSGI config for myalumini project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
#
## assuming your django settings file is at '/home/chandanmanna48/mysite/mysite/settings.py'
## and your manage.py is is at '/home/chandanmanna48/mysite/manage.py'
path = '/home/chandanmanna48/AluminiNIT/myalumini'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myalumini.settings")

application = get_wsgi_application()

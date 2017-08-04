__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"
"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os
import sys

janeway_path = '/path/to/installation' # This is the directory where you cloned janeway (ie. "/Users/me/Projects/janeway")
virtualenv_path = '/path/to/your/virtualenv/name'
virtualenv_python_verison = 3.6 # two digits only (ie. if python3 -V says "Python 3.5.7", this would be 3.5)

# add the project path into the sys.path:
sys.path.append(os.path.join(janeway_path, 'src'))
# add the site-packages folder to sys.path:
sys.path.append(os.path.join(virtualenv_path, 'lib', 'python'+str(virtualenv_python_verison), 'site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
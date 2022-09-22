"""
Project WSGI deployemnt configuration 
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_fetch_api.settings')

application = get_wsgi_application()

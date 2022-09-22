"""
ASGI deployment configuration of the project
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_fetch_api.settings')

application = get_asgi_application()

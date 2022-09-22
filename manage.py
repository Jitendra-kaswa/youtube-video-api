
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # setting up the default setting page
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'youtube_fetch_api.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

#!/usr/bin/env python
import sys

if __name__ == "__main__":

    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=[
            'south',
            'nonprofit.funding',
            'nonprofit.mailroom',
            'nonprofit.staff',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'dev.db',
            },
        }
    )

    execute_from_command_line(sys.argv)

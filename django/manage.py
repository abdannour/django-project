"""Django's command-line utility for administrative tasks.

This file is the standard entry point used by `manage.py` to run
management commands such as `runserver`, `migrate`, and `createsuperuser`.
"""

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tp_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "error when importing Django."
        ) from exc
    execute_from_command_line(sys.argv)

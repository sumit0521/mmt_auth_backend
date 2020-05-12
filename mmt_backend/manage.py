#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

env_name = os.environ.setdefault("CURR_ENV", "PROD").upper()
proj_name = 'mmt_backend'
if env_name in {"DEV", "DEVEL"}:
    root_path = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..'))
    sys.path.insert(0, os.path.abspath(os.path.join(root_path, proj_name)))
    sys.path.insert(0, os.path.abspath(os.path.join(root_path, proj_name, proj_name)))
    print(sys.path)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmt_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#!/bin/bash

# Apply database migrations
# echo "Apply database migrations"
# python manage.py migrate

# Start server
echo "Starting server"
gunicorn employees.wsgi:application -w 2 -b :8000
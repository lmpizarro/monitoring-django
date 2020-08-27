#!/bin/sh

python manage.py flush --noinput
python manage.py migrate --noinput
python manage.py createsuperuser2 --username admin --password admin --noinput --email 'blank@email.com'
python manage.py init_db
python manage.py collectstatic --no-input
gunicorn birras.wsgi:application  --workers=4 --log-file=- --log-level=info --bind 0.0.0.0:8080

exec "$@"

#!/bin/sh

if [ "$CONTAINER" = "web" ]
then
    echo "running container web"
    python manage.py flush --noinput
    python manage.py migrate --noinput
    python manage.py createsuperuser2 --username admin --password admin --noinput --email 'blank@email.com'
    python manage.py init_db
    python manage.py collectstatic --no-input
    gunicorn -c gunicorn.py birras.wsgi:application    
fi
exec "$@"

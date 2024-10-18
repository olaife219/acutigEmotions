release: python manage.py migrate
web: daphne cardealer.asgi:application -b 0.0.0.0 -p $PORT

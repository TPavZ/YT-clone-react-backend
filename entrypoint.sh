#set -e #exit for errors

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@gmail.com

python ./drf_jwt_backend/manage.py migrate

python ./drf_jwt_backend/manage.py createsuperuser --noinput

python ./drf_jwt_backend/manage.py runserver 0.0.0.0:8000
#!/bin/bash

while ! PGPASSWORD=${POSTGRES_PASSWORD} pg_isready -h postgres -U ${POSTGRES_USER} -d ${POSTGRES_DB}
do
  echo "Aguardando o PostgreSQL inicializar..."
  sleep 5
done

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate

uwsgi --ini infra/uwsgi/mutation-analyzer-uwsgi.ini
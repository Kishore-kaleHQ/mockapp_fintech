#!/bin/bash
set -e

# Maximum number of attempts
MAX_ATTEMPTS=30
ATTEMPTS=0

echo "Waiting for postgres..."
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  ATTEMPTS=$((ATTEMPTS+1))
  if [ $ATTEMPTS -ge $MAX_ATTEMPTS ]; then
    echo "Timeout waiting for Postgres"
    exit 1
  fi
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "PostgreSQL started"

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Starting Gunicorn..."
gunicorn mockapp_fintech.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 4 \
    --timeout 90 \
    --access-logfile '-' \
    --error-logfile '-' \
    --log-level info
#!/bin/sh

# Wait for the database to be ready (if you are using a database)
# Here's an example for PostgreSQL:
# while ! nc -z db 5432; do
#   sleep 0.5
# done

# Run migrations
python3 manage.py migrate

# Create default user
python3 manage.py create_default_user

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic --noinput


# Start your application
exec "$@"
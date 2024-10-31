port := 8000
worker := 5
concurrency := 2

check:
	python manage.py check

shell:
	python manage.py shell

dev:
	python manage.py runserver

start:
	python manage.py collectstatic --no-input
	python manage.py crontab add
	gunicorn config.wsgi -w $(worker) -b 127.0.0.1:$(port)

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

seed:
	python manage.py seed

celery:
	celery -A src worker --loglevel=debug --concurrency=$(concurrency)

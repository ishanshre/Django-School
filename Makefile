run:
	python manage.py runserver

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser


tailwindcss:
	npx tailwindcss -i ./static/base.css -o ./static/styles.css --watch

run:
	python3 ./manage.py collectstatic --noinput
	python3 ./manage.py migrate
	systemctl restart gunicorn.service

run:
	git pull
	rm -rf ./staticfiles
	python3 ./manage.py collectstatic --noinput
	python3 ./manage.py migrate
	systemctl restart gunicorn.service

production:
	pip install -r ./requirements/production.txt

development:
	pip install -r ./requirements/development.txt

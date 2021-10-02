.PHONY: user-seed
user-seed:
	venv/bin/python manage.py seed auth --number 10

.PHONY: docker-up
docker-up:
	docker compose up --build
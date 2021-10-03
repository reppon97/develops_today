.PHONY: user-seed
user-seed:
	venv/bin/python manage.py seed auth --number 10

.PHONY: docker-up
docker-up:
	docker compose up --build

.PHONY: db-init
db-init:
	docker-compose up -d --build
	docker exec develops_today_api_1 bash -c "python manage.py makemigrations post"
	docker exec develops_today_api_1 bash -c "python manage.py migrate"
	docker exec develops_today_api_1 bash -c "python manage.py seed post --number 10"
	docker-compose down

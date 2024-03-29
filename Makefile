.PHONY: user-seed
user-seed:
	venv/bin/python manage.py seed auth --number 10

.PHONY: docker-up
docker-up:
	docker-compose up -d
	docker exec develops_today_api_1 bash -c "python manage.py makemigrations post"
	docker exec develops_today_api_1 bash -c "python manage.py migrate"

.PHONY: db-seed
db-seed:
	docker exec develops_today_api_1 bash -c "python manage.py seed post --number 10"

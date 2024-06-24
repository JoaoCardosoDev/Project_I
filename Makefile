docker: 
	docker-compose up

# Criar BD e aplicar migrações
migration: docker
	python manage.py makemigrations && python manage.py migrate


# Up e down do projeto
up: migration
	python manage.py runserver

down:
	docker-compose down

# Criar super user
superuser:
	python manage.py createsuperuser
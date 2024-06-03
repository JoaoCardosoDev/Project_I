docker: 
	docker-compose up

# Criar BD e aplicar migrações
migration: docker
	cd EticDrive && python manage.py makemigrations && python manage.py migrate


# Up e down do projeto
up: migration
	cd EticDrive && python manage.py runserver

down:
	docker-compose down

# Criar super user
superuser:
	cd EticDrive && python manage.py createsuperuser
docker: 
	docker-compose up

# Criar BD e aplicar migrações
migration: 
	python manage.py makemigrations && python manage.py migrate


# Up e down do projeto
up: 
	python manage.py runserver

down:
	docker-compose down

# Criar super user
superuser:
	python manage.py createsuperuser

create_superuser:
	@echo "Creating superuser..."
	@echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@test.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python3 manage.py shell

freshstart: migration create_superuser up
	
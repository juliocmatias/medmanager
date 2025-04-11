# Caminhos dos diretórios do projeto
APP_DIRS = core medmanager tests

# Comando para rodar os testes com pytest
test:
	poetry run pytest

# Comando para verificar lint com flake8
lint:
	poetry run flake8 $(APP_DIRS)

# Comando para formatar com black e isort
format:
	poetry run isort $(APP_DIRS)
	poetry run black $(APP_DIRS)

# Comando para verificar se o código está formatado corretamente
check-format:
	poetry run black --check $(APP_DIRS)
	poetry run isort --check-only $(APP_DIRS)

# Comando para roda a aplicação
run:
	poetry run python manage.py runserver

# Comando para rodar o servidor de desenvolvimento
dev:
	poetry run python manage.py runserver 0.0.0.0:8000

test-cov:
	poetry run pytest --cov=$(APP_DIRS) --cov-report=term-missing

test-cov-html:
	poetry run pytest --cov=core --cov-report=html

# Aplicar as migrações
migrate:
	poetry run python manage.py migrate

# Criar novas migrações
makemigrations:
	poetry run python manage.py makemigrations

# Criar superusuário
superuser:
	poetry run python manage.py createsuperuser

# Carregar dados de fixtures (ex: users.json)
load-fixtures:
	poetry run python manage.py loaddata

# Ver status das migrações
showmigrations:
	poetry run python manage.py showmigrations

# Abrir o shell do Django
shell:
	poetry run python manage.py shell

.PHONY: test lint format check-format run dev test-cov migrate makemigrations superuser load-fixtures showmigrations shell test-cov-html
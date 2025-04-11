.PHONY: help run test lint format

help:
	@echo "Comandos disponíveis:"
	@echo "  make run        - Executa o servidor de desenvolvimento"
	@echo "  make test       - Roda os testes com pytest"
	@echo "  make lint       - Verifica padrões com flake8 e isort"
	@echo "  make format     - Formata o código com black e isort"

run:
	poetry run python manage.py runserver

test:
	poetry run pytest

lint:
	poetry run flake8 .
	poetry run isort . --check-only

format:
	poetry run black .
	poetry run isort .

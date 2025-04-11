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

.PHONY: test lint format check-format
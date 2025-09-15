# Makefile для удобного запуска команд

# Запуск приложения локально
run:
	docker-compose up --build

# Unit-тесты
test:
	pytest app/tests

# Линтер
lint:
	flake8 app

# SAST анализ
scan:
	bandit -r app
	semgrep --config=auto app
	pip-audit

# Полный цикл: тесты + линт + анализ
all: test lint scan

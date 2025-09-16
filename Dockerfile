# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Копируем зависимости и ставим их
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Копируем установленные пакеты из builder
COPY --from=builder /usr/local /usr/local

# Копируем код приложения
COPY app/ .

# Создаём непривилегированного пользователя
RUN useradd -m nonroot
USER nonroot

# Открываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]


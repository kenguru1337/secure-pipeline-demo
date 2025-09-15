# Stage 1: build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app/ .
RUN useradd -m nonroot
USER nonroot
CMD ["python", "app.py"]
# Stage 1: build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app/ .
RUN useradd -m nonroot
USER nonroot
CMD ["python", "app.py"]


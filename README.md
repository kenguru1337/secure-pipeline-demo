# 🔐 Secure CI/CD Pipeline Demo

Учебный проект, демонстрирующий **CI/CD пайплайн с элементами безопасности** для Python Flask-приложения.  
Подходит для демонстрации навыков **DevOps / DevSecOps / AppSec (junior level)**. 
---

## 📌 Возможности проекта
- ✅ Простое веб-приложение на Flask  
- ✅ Контейнеризация (Docker, Docker Compose)  
- ✅ CI/CD пайплайн на GitHub Actions  
- ✅ Интеграция инструментов безопасности:
  - **Bandit** — статический анализ Python-кода  
  - **Semgrep** — поиск уязвимостей и ошибок  
  - **Trivy** — сканирование Docker-образов  
  - **pip-audit** — проверка зависимостей  
  - **flake8** — проверка качества кода  

---

## 📂 Структура репозитория
```console
secure-pipeline-demo/
│── app/
│   ├── app.py                    # Flask-приложение
│   ├── requirements.txt          # Python-зависимости
│   └── tests/                    # Тесты
│       └── test_app.py           # Unit-тесты
│
│── .github/                      # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml                # CI/CD пайплайн
│
│── Dockerfile                    # Docker-образ приложения
│── docker-compose.yml            # Локальный запуск через Docker Compose
│── Makefile
│── .gitignore
│── README.md                     # Документация проекта
```
---

## ⚙️ Требования
- [Python 3.11+](https://www.python.org/downloads/)  
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)  
- GitHub-аккаунт (для запуска CI/CD)  

---

## 🚀 Установка и запуск локально

### 1. Клонировать репозиторий
```bash
git clone https://github.com/username/secure-pipeline-demo.git
cd secure-pipeline-demo
```
### 2. Создать виртуальное окружение Python
```bash
# для Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```
```bash
# для Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate
```
### 3. Установить зависимости
```bash
pip install --upgrade pip
pip install -r app/requirements.txt
```
### 4. Запустить приложение
```bash
cd app
python app.py
```
По умолчанию Flask запустится на <http://127.0.0.1:5000>\

### 5. Проверка API
```console
curl http://127.0.0.1:5000
# Ответ: {"message": "Hello from Secure CI/CD Pipeline!"}

curl http://127.0.0.1:5000/health
# Ответ: {"status": "ok"}
```
### 6. Запустить unit-тесты
```bash
pytest app/tests
```

##  🐳 Docker и Docker Compose
```bash
docker build -t secure-pipeline-demo .
docker run -p 5000:5000 secure-pipeline-demo
```
Локальный запуск через Docker Compose
```bash
docker-compose up --build
```
Теперь приложение доступно на 👉 http://localhost:5000

## 🧪 Makefile команды
```bash
| Команда     | Описание                                   |
| ----------- | ------------------------------------------ |
| `make run`  | Запуск приложения через Docker Compose     |
| `make test` | Запуск unit-тестов                         |
| `make lint` | Проверка кода flake8                       |
| `make scan` | SAST анализ (Bandit + Semgrep + pip-audit) |
| `make all`  | Полный цикл: тесты + линт + анализ         |

```
## ⚡ CI/CD Workflow
Пайплайн запускается при push или pull request в main и выполняет:
1. Unit-тесты (pytest)
2. Static Application Security Testing (SAST)
   * Bandit, Semgrep
3. Dependency scan — pip-audit
4. Lint — flake8
5. Docker build
6. Docker image scan — Trivy
7. Публикация Docker-образа в GitHub Container Registry

## 📊 Схема пайплайна
```bash
flowchart TD
    A[Push/Pull Request] --> B[Install Dependencies]
    B --> C[Run Unit Tests]
    C --> D[Bandit Analysis]
    C --> E[Semgrep Analysis]
    C --> F[pip-audit]
    C --> G[flake8 Lint]
    D --> H[Docker Build]
    E --> H
    F --> H
    G --> H
    H --> I[Trivy Scan]
    I --> J[Push Docker Image to GHCR]

```
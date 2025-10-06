FROM python:3.11-slim

# Робоча директорія всередині контейнера
WORKDIR /app

# Встановити системні залежності, потрібні для mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Скопіювати requirements
COPY requirements.txt /app/

# Встановити Python-залежності
RUN pip install --no-cache-dir -r requirements.txt

# Скопіювати увесь код у контейнер
COPY . /app

# Запускаємо gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]

# Додаємо healthcheck (опціонально)
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

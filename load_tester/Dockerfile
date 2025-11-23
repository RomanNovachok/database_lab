FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY load.py /app/

CMD ["python", "load.py"]

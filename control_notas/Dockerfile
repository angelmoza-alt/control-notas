FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SECRET_KEY="prod-secret-key-change-me"
ENV DEBUG="False"
ENV USE_SQLITE="True"
ENV PORT=8080

RUN python manage.py collectstatic --noinput
RUN USE_SQLITE=True python manage.py migrate --noinput

EXPOSE 8080

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8080", "--workers", "2"]

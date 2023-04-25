FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    pip install --upgrade pip && \
    pip install psycopg2-binary

COPY requirements/requirements.txt requirements/requirements.txt

RUN pip install -r requirements/requirements.txt

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

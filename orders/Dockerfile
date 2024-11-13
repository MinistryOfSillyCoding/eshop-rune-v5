FROM python:latest

WORKDIR /app

RUN pip install flask flask-sqlalchemy psycopg2-binary

COPY . .

EXPOSE 5000

CMD [ "python", "main.py"]
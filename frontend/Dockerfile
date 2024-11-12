FROM python:latest

WORKDIR /app

RUN pip install requests flask

COPY . .

EXPOSE 5000

CMD [ "python", "main.py"]
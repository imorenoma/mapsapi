FROM python:3.10.6-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 6000

CMD ["python", "app.py"]



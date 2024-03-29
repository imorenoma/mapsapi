FROM python:3.10.6-slim

WORKDIR /app

COPY . /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
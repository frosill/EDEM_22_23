FROM python:3.10-slim-bullseye

COPY main.py /app/
COPY requirements.txt /app/

WORKDIR /app

RUN apt-get update

RUN pip install mysql-connector-python

CMD ["python3", "main.py"]

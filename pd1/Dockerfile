FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY pd1.py .

ENV FLASK_APP=pd1

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

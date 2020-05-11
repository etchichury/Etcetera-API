FROM python:3.8

WORKDIR /app

COPY . /app

ENV FLASK_APP=src

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
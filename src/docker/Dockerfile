FROM python:3.8

WORKDIR /app

COPY . /app

# Prevents from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0"]
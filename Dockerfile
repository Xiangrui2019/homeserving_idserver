FROM python:latest

WORKDIR /app
EXPOSE 80
RUN pip install pipenv
COPY . .
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python3", "manage.py", "runserver", "0.0.0.0:80"]

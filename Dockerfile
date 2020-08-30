FROM pypy:3

WORKDIR /app
EXPOSE 80
RUN pip install pipenv
COPY . .
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "pypy3", "manage.py", "runserver", "0.0.0.0:80"]

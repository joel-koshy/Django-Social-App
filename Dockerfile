FROM python:3.10

WORKDIR /code 

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv 
RUN pipenv install --system 

COPY . /code/

ENV PORT 8000 

CMD gunicorn --bind :$PORT --workers 3 config.wsgi
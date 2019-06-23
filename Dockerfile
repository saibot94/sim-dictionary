FROM python:3.7-alpine

RUN pip install pipenv

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1

COPY . /app
WORKDIR /app


RUN pipenv install --system --deploy --ignore-pipfile

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]


FROM python:3.7-alpine

EXPOSE 8000
ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1

RUN pip install pipenv

COPY . /app
WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["gunicorn", "run:app"]


# Similarity dictionary

Simple scraper / dictionary app with an intuitive interface.

## Endpoints

- `/api/translations/<word>`: get all the translations in all languages for a word

## Developing

Install all dependencies (will initiate a new virtualenvironment)

```bash
pipenv install
```

If any issues are encountered:

```bash
pipenv lock --pre --clear
pipenv install
```

To run:

```bash
FLASK_DEBUG=1 FLASK_APP="run.py" flask run --host 0.0.0.0
```
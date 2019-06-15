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

To add a new crawler:

- in the crawlers module add a `<language>_crawler.py` file, which contains the crawler itself. 
- in `__init__.py` follow the example: ``

## Populating with data

To populate the DB for a language based on the seed data:

```bash
python crawler_cli.py --name "Romanian"
```

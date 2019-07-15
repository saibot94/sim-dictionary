# Similarity dictionary

[![Build Status](https://travis-ci.org/saibot94/sim-dictionary.svg?branch=master)](https://travis-ci.org/saibot94/sim-dictionary)

Simple scraper / dictionary app with an intuitive interface.

## Endpoints

- `/api/translations/<word>`: get all the translations in all languages for a word
- `/api/translations?q=so*`: get all english words that can be used. You can search through them by using a * operator. Or something like `q=*o*`

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
FLASK_DEBUG=1 FLASK_APP="src/run.py" flask run --host 0.0.0.0
```

To run on windows (powershell):

```powershell
 $env:FLASK_DEBUG=1; $env:FLASK_APP="src/run.py"; flask run
 ```

To add a new crawler:

- in the crawlers module add a `<language>_crawler.py` file, which contains the crawler itself. 
- in `__init__.py` follow the example: ``

## Populating with data

Use the `crawler_cli.py` script in the src folder:

```text
usage: crawler_cli [-h] [--crawlers CRAWLERS] name

Seed things as fast as possible using this simple tool

positional arguments:
  name                 The name of the language

optional arguments:
  -h, --help           show this help message and exit
  --crawlers CRAWLERS  Module from where the crawlers should be loaded
```

To populate the DB for a language based on the seed data:

```bash
python src/crawler_cli.py "Romanian"
```

or on Windows: 

```powershell
python .\src\crawler_cli.py "Romanian"
```

import click
import importlib
from sim_dict import db
from sim_dict.models import Language, Translation
from sim_dict.constants import SEED_WORDS
import argparse

def populate(crawler, lang):
    for word in SEED_WORDS:
        try:
            for translation in crawler.get_word(word):
                existing = Translation.query.filter_by(
                    en_word=word, translation=translation
                ).first()
                if existing:
                    print(
                        "ERR: translation for '{}' in lang '{}' exists!".format(
                            word, lang.display_name
                        )
                    )
                    continue
                new_translation = Translation(
                    en_word=word, translation=translation, language_id=lang.id
                )
                if translation:
                    db.session.add(new_translation)
                    print("Added '{}' -> '{}'".format(word, translation))
        except Exception as e:
            print("EX: word: '{}', e: {}".format(word, e))
    db.session.commit()

def crawler_cli():
    """Simple to trigger the crawling of a language."""

    parser = argparse.ArgumentParser("crawler_cli", description="Seed things as fast as possible using this simple tool")
    parser.add_argument("name", help="The name of the language", type=str)
    parser.add_argument("--crawlers", help="Module from where the crawlers should be loaded", type=str, default="sim_dict.crawlers")

    args = parser.parse_args()

    lang = Language.query.filter_by(display_name=args.name).first()
    if not lang:
        print("ERROR: Language with this name not found")
        return

    crawlers_module = importlib.import_module(args.crawlers)
    crawler = getattr(crawlers_module, lang.crawler)
    if not crawler:
        print("ERROR: Crawler '{}' not found".format(lang.crawler))
        return
    populate(crawler, lang)


if __name__ == "__main__":
    crawler_cli()

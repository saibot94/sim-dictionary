import click
import importlib
from sim_dict import db
from sim_dict.models import Language, Translation

SEED_WORDS = [
    "the",
    "be",
    "to",
    "of",
    "and",
    "a",
    "in",
    "that",
    "have",
    "I",
    "it",
    "for",
    "not",
    "on",
    "with",
    "as",
    "you",
    "do",
    "at",
    "this",
    "but",
    "his",
    "by",
    "from",
    "they",
    "we",
    "say",
    "her",
    "she",
    "or",
    "an",
    "will",
    "my",
    "one",
    "all",
    "would",
    "there",
    "their",
    "what",
    "so",
    "up",
    "out",
    "if",
    "about",
    "who",
    "get",
    "which",
    "go",
    "me",
    "when",
    "make",
    "can",
    "like",
    "time",
    "no",
    "just",
    "him",
    "know",
    "take",
    "people",
    "into",
    "year",
    "your",
    "good",
    "some",
    "could",
    "them",
    "see",
    "other",
    "than",
    "then",
    "now",
    "look",
    "only",
    "come",
    "its",
    "over",
    "think",
    "also",
    "back",
    "after",
    "use",
    "two",
    "how",
    "our",
    "work",
    "first",
    "well",
    "way",
    "even",
    "new",
    "want",
    "because",
    "any",
    "these",
    "give",
    "day",
    "most",
    "us",
]


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


@click.command()
@click.option("--name", help="Name of the language.", type=str)
@click.option(
    "--crawlersmod",
    help="Module from where to load the crawlers.",
    type=str,
    default="sim_dict.crawlers",
)
def crawler_cli(name, crawlersmod):
    """Simple to trigger the crawling of a language."""
    lang = Language.query.filter_by(display_name=name).first()
    if not lang:
        print("ERROR: Language with this name not found")
        return

    crawlers_module = importlib.import_module(crawlersmod)
    crawler = getattr(crawlers_module, lang.crawler)
    if not crawler:
        print("ERROR: Crawler '{}' not found".format(lang.crawler))
        return
    populate(crawler, lang)


if __name__ == "__main__":
    crawler_cli()

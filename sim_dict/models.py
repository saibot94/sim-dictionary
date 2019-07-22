import logging
from sim_dict import db, ma


class Language(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    display_name = db.Column(db.String(), nullable=False)
    crawler = db.Column(db.String(), nullable=False)
    language_code = db.Column(db.String(), nullable=False, default="Unknown")

    def __repr__(self):
        return "<Language {} >".format(self.display_name)


class Translation(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    en_word = db.Column(db.String(), nullable=False)
    translation = db.Column(db.String(), nullable=False, default="Unknown")
    language_id = db.Column(
        db.Integer, db.ForeignKey("language.id"), nullable=True)
    language = db.relationship("Language", backref="words")

    def __repr__(self):
        return "<Translation '{}' -> '{}' >".format(self.en_word, self.translation)


class TranslationSchema(ma.ModelSchema):
    class Meta:
        model = Translation


class LanguageSchema(ma.ModelSchema):
    class Meta:
        model = Language


translation_schema = TranslationSchema()
lang_schema = LanguageSchema()

SEED_LANGUAGES = [Language(id=1, display_name="Romanian", crawler="romanian_crawler", language_code="RO"), Language(
    id=2, display_name="Polish", crawler="polish_crawler", language_code="PL")]


def seed_data():
    for lang in SEED_LANGUAGES:
        found = Language.query.get(lang.id)
        if not found:
            logging.info("Adding lang: {}".format(lang))
            db.session.add(lang)
        else:
            print('updating...')
            Language.query.filter_by(id=lang.id).update(
                {'display_name': lang.display_name, 'crawler': lang.crawler, 'language_code': lang.language_code})
    db.session.commit()

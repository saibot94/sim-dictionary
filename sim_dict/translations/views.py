from flask import jsonify, request
from sim_dict.translations import mod_translations
from sim_dict.models import Translation, Language, translation_schema


@mod_translations.route("/<word>", methods=["GET"])
def get_all_for_word(word):
    translations = Translation.query.filter_by(en_word=word).all()
    data = translation_schema.dump(translations, many=True)
    for item in data:
        lang = Language.query.get(item["language"])
        item["language_name"] = lang.display_name
    return jsonify({"data": data})


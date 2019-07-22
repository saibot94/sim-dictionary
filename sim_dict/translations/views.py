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
        item["language_code"] = lang.language_code
    return jsonify({"data": data})


@mod_translations.route("/", methods=["GET"])
def get_possible_words():
    query = request.args.get("q")
    translations = None
    if query:
        query = query.replace("*", "%")
        translations = Translation.query.filter(Translation.en_word.ilike(query)).all()
    else:
        translations = Translation.query.all()
    en_words = list(set(map(lambda t: t.en_word, translations)))
    return jsonify({"data": en_words})

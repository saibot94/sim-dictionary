from flask import jsonify, request
from sim_dict.translations import mod_translations


@mod_translations.route("/<word>", methods=["GET"])
def get_all_for_word(word):
    return jsonify({"word": word})


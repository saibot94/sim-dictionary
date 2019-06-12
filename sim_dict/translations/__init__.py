from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
    jsonify,
)

from flask_sqlalchemy import SQLAlchemy
from sim_dict import db

mod_translations = Blueprint("translations", __name__, url_prefix="/api/translations")

import sim_dict.translations.views
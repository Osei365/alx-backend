#!/usr/bin/env python3
"""flask app."""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """config class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """gets a particular user."""
    user_id = request.args.get('login_as')
    if user_id:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """runs before every app."""
    setattr(g, 'user', get_user())
    


@babel.localeselector
def get_locale():
    """gets local language."""
    lang = request.args.get('locale')
    if lang in Config.LANGUAGES:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index view handler."""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()

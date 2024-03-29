#!/usr/bin/env python3
"""flask app."""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
import datetime


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
    g.time = format_datetime(datetime.datetime.now())


@babel.localeselector
def get_locale():
    """gets local language."""
    options = [
        request.args.get('locale'),
        g.user.get('locale') if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@babel.timezoneselector
def get_timezone() -> str:
    """Gets time zone."""
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """index view handler."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

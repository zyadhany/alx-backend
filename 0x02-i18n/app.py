#!/usr/bin/env python3
"""
simple Flask
"""

import flask
import pytz
from flask import Flask, render_template, request
from flask_babel import Babel, format_datetime


class Config:
    """
    Config class
    """

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


def get_user() -> dict:
    """
    get user
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users[user_id]
    except Exception:
        return None


@app.before_request
def before_request():
    """
    before request
    """
    flask.g.user = get_user()
    flask.g.time = format_datetime()


@babel.localeselector
def get_locale() -> str:
    """
    get locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    user = get_user()
    if user:
        locale = user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    get timezone
    """
    local = request.args.get('timezone')
    if not local:
        user = get_user()
        if user:
            local = user.get('timezone')

    if local:
        try:
            return pytz.timezone(local).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    return string
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

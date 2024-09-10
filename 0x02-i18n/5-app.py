#!/usr/bin/env python3
"""
simple Flask
"""

import flask
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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


@babel.localeselector
def get_locale() -> str:
    """
    get locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


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

@app.route('/')
def index() -> str:
    """
    return string
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

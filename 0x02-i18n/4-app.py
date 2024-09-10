#!/usr/bin/env python3
"""
simple Flask
"""

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


@app.route('/')
def index() -> str:
    """
    return string
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

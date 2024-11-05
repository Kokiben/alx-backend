#!/usr/bin/env python3
"""
Flask app with Babel integration, locale selection, and template translations.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """App configuration class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Check if the locale is passed in the request
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fall back to the best match if not set
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page with a welcome message."""
    return render_template('4-index.html')


# This condition checks if the script is run directly
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

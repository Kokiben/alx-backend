#!/usr/bin/env python3
"""
Basic Flask app with a single route and a simple HTML template.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)


@babel.localeselector
def get_locale():
    # Check if 'locale' is passed as a query parameter
    locale = request.args.get('locale')
    if locale and locale in ['en', 'fr']:
        return locale
    # Fall back to the default behavior (e.g., accept languages)
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    """Render the index page with a welcome message."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port=5000)

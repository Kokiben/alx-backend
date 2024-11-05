#!/usr/bin/env python3
"""
Basic Flask app with a mock user login system and locale handling.
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return a user dictionary or None if no user is found."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Set the user globally using get_user."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Check for locale in URL parameters
    locale = request.args.get('locale')
    if locale:
        return locale

    # Check for locale in user settings
    if g.user and g.user.get('locale'):
        return g.user['locale']

    # Check for locale in request headers
    if request.accept_languages:
        return request.accept_languages.best_match(['en', 'fr', 'kg'])

    # Fallback to default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Render the index page."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(port=5000)

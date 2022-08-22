from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-springboard',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-springboard")))
    app.add_html_theme(
        'handouts-springboard',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-springboard")))

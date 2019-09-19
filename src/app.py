from datetime import datetime

from flask import Flask, render_template, request, Blueprint

from sections import events

blueprints = [
    events.bp,
]

app = Flask(__name__)
for bp in blueprints:
    app.register_blueprint(bp)


@app.context_processor
def add_navigation() -> dict:
    endpoints = [(f'{bp.name}.index', bp.name.title()) for bp in blueprints]
    items = [{
        'active': request.endpoint == endpoint,
        'endpoint': endpoint,
        'title': title,
    } for endpoint, title in endpoints]

    return {
        'navigation': items,
    }


@app.context_processor
def add_last_updated() -> dict:
    """
    Returns the date when the website was updated.
    Since we are using frozen-flask, we just return datetime.now()
    :return:
    """
    return {
        'PAGE_LAST_UPDATED': datetime.now().strftime('%c')
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

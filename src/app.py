#!/usr/bin/env python3

from datetime import datetime

from flask import Flask, render_template, request

from sections import events, projects, running_expenses

blueprints = [
    (events.bp, None),
    (projects.bp, None),
    (running_expenses.bp, 'Laufende Kosten'),
]

app = Flask(__name__)
for bp, _ in blueprints:
    app.register_blueprint(bp)


@app.context_processor
def add_navigation() -> dict:
    endpoints = [(f'{bp.name}.index', title or bp.name.title()) for bp, title in blueprints]
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


if __name__ == '__main__':
    app.run()

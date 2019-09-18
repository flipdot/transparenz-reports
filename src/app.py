from flask import Flask, render_template, request, Blueprint

from fizzbuzz import fizzbuzz

bp = Blueprint('main', __name__, template_folder='templates')


@bp.context_processor
def add_navigation() -> dict:
    endpoints = [
        ('main.index', 'Home'),
        ('main.about', 'About')
    ]
    items = [{
        'active': request.endpoint == endpoint,
        'endpoint': endpoint,
        'title': title,
    } for endpoint, title in endpoints]

    return {
        'navigation': items,
    }


@bp.route('/')
def index():
    results = [{
        'input': x,
        'output': fizzbuzz(x),
    } for x in range(25, 41)]
    return render_template('index.html', results=results)


@bp.route('/about/')
def about():
    return render_template('about.html')


app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()

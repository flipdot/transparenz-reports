from flask import Blueprint, render_template, abort, jsonify
import pandas as pd
from pathlib import Path

bp = Blueprint('running_expenses', __name__, url_prefix='/betriebskosten', template_folder='templates')


@bp.route('/')
def index():
    categories = {
        'hcloud': 'Server'
    }
    return render_template('running_expenses/index.html', categories=categories)


@bp.route('/data/<category>.json')
def category_data(category):
    if category == 'hcloud':
        costs = get_costs_hcloud()
        return jsonify(costs)
    elif category == 'total':
        return jsonify([{
            'x': [0, 1, 2, 3, 4, 5],
            'y': [3, 3, 3, 1, 8, 5],
            'name': 'tot',
            'type': 'scatter',
        }])
    abort(404)


def get_costs_hcloud():
    path = Path('data/running_expenses/hcloud/')
    projects = {}
    for csv_path in sorted(path.glob('*.csv')):
        data = pd.read_csv(csv_path)
        for name, group in data.groupby('project'):
            if not name in projects:
                projects[name] = {'x': [], 'y': [], 'type': 'scatter', 'name': name, 'stackgroup': 'one'}
            p = projects[name]
            group = group.sort_values('day_to')
            if not (group['day_to'].any() == group['day_to']).all():
                abort(500, 'Some day_to are not equal')
            p['x'].append(group['day_to'].any())
            p['y'].append(group['price_netto'].sum() * 1.19)

    return list(projects.values())
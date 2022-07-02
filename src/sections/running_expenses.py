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
        all_costs = {
            'Server': get_costs_hcloud(),
        }
        res = []
        for k, v in all_costs.items():
            cummulated = {}
            for e in v:
                for i, day in enumerate(e['x']):
                    cummulated[day] = cummulated.get(day, 0) + e['y'][i]
            x = sorted(cummulated.keys())
            y = [cummulated[key] for key in x]

            res.append({
                'x': x,
                'y': y,
                'name': k,
                'type': 'scatter',
                'stackgroup': 'one',
            })
        return jsonify(res)
    abort(404)


def get_costs_hcloud():
    path = Path('data/running_expenses/hcloud/')
    projects = {}
    for csv_path in sorted(path.glob('????-??-??.csv')):
        data = pd.read_csv(csv_path)
        for name, group in data.groupby('project'):
            if name not in projects:
                projects[name] = {'x': [], 'y': [], 'type': 'scatter', 'name': name, 'stackgroup': 'one'}
            p = projects[name]
            group = group.sort_values('date_to')
            if n := len(group["date_to"].value_counts()) != 1:
                raise ValueError(f"All date_to should be the same, but there are {n} different values")
            p['x'].append(group['date_to'].iloc[0])
            p['y'].append(group['price_gross'].sum())

    return list(projects.values())

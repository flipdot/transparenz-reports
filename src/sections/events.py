import re
from typing import List, Dict, Union

from flask import Blueprint, render_template
from pathlib import Path
import yaml

bp = Blueprint('events', __name__, url_prefix='/events', template_folder='templates')


def create_cost_table(data, title=None, depth=0) -> List[Dict[str, Union[str, float, bool]]]:
    result = []
    for element in data:
        description = ' – '.join(filter(None, [title, element['title']]))
        if 'items' in element:
            sub_elements = create_cost_table(element['items'], description, depth + 1)
            result += sub_elements
        else:
            result.append({
                'description': description,
                'amount': element['amount'],
                'depth': depth,
                'estimate': element.get('estimate'),
            })
    description = ' – '.join(filter(None, [title, 'SUMME']))
    sub_sum = sum([x['amount'] for x in result if not x.get('is_sum')])
    result.append({'description': description, 'amount': sub_sum, 'is_sum': True, 'depth': depth})
    return result


@bp.route('/')
def index():
    events_path = Path('data/events/')
    paths = events_path.glob('**/*.yml')
    event_list = [re.search(r'(\d+)/(.+).yml', str(p)).groups() for p in paths]
    return render_template('events/index.html', event_list=event_list)


@bp.route('/<string:year>/<string:event_name>/')
def event(year, event_name):
    with open(Path('data/events') / year / f'{event_name}.yml') as f:
        event_data = yaml.safe_load(f)
    expenditures = create_cost_table(event_data['expenditures'])
    revenues = create_cost_table(event_data['revenues'])
    total_expenditure = sum([x['amount'] for x in expenditures if not x.get('is_sum')])
    total_revenue = sum([x['amount'] for x in revenues if not x.get('is_sum')])
    return render_template('events/detail.html',
                           event=event_data,
                           expenditures=expenditures,
                           revenues=revenues,
                           total_expenditure=total_expenditure,
                           total_revenue=total_revenue,
                           )

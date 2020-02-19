from flask import Blueprint, render_template
from pathlib import Path
import yaml

bp = Blueprint('projekte', __name__, url_prefix='/projekte', template_folder='templates')


@bp.route('/')
def index():
    with open(Path('data/projects.yml')) as f:
        data = yaml.safe_load(f)
    for year, projects in data.items():
        for project in projects:
            project['total_costs'] = sum([x['price'] * x.get('quantity', 1) for x in project['costs']])
    return render_template('projects/index.html', data=data)

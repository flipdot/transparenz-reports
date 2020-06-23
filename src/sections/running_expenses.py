from flask import Blueprint, render_template

bp = Blueprint('laufende kosten', __name__, url_prefix='/betriebskosten', template_folder='templates')


@bp.route('/')
def index():
    return render_template('running_expenses/index.html')

from flask import Blueprint, render_template

bp = Blueprint('events', __name__, url_prefix='/events', template_folder='templates')


@bp.route('/index')
def index():
    return render_template('events/index.html')

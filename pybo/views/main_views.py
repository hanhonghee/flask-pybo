from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
#@bp.route('/question/list')
def index():
    #question, _list 순서로 해석되어 함수명을 찾아준다
    return redirect(url_for('question._list'))

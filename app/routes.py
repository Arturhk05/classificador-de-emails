from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Página Inicial')

@bp.route('/api/classify', methods=['POST'])
def classify_email():
    #TODO: Implementar lógica para classificação de e-mails
    pass
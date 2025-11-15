from flask import Blueprint, render_template, request
from app.email_classifier import EmailClassifier

bp = Blueprint('main', __name__)

classifier = EmailClassifier()

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Página Inicial')

@bp.route('/api/classify', methods=['POST'])
def classify_email():
    data = request.get_json()
    email_text = data.get('email_text', '')

    result = classifier.classify_and_respond(email_text)

    return {
        'category': result['category'],
        'response': result['suggested_response'],
        'processed_text': result['processed_text']
    }
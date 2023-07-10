from flask import Blueprint, render_template, request
from .models import db, Thesis

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        thesis_title = request.form['thesis_title']
        thesis_abstract = request.form['thesis_abstract']
        thesis = Thesis(title=thesis_title, abstract=thesis_abstract)
        db.session.add(thesis)
        db.session.commit()
        return 'Thesis saved successfully'

    return render_template('home.html')


from flask import Blueprint, render_template, request, flash, redirect
from .models import db, Thesis

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    theses = Thesis.query.all()
    return render_template('home.html', theses=theses)


@views.route('/backend', methods=['GET', 'POST'])
def backend():
    if request.method == 'POST':
        thesis_title = request.form['thesis_title']
        thesis_abstract = request.form['thesis_abstract']
        thesis = Thesis(title=thesis_title, abstract=thesis_abstract)
        db.session.add(thesis)
        db.session.commit()
        flash('Thesis saved successfully')  # Store success message
        return redirect('/')  # Redirect to home page

    theses = Thesis.query.all()
    return render_template('home.html', theses=theses)

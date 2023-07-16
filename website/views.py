from flask import Blueprint, render_template, request, flash, redirect
from .models import db, Thesis
from flask import jsonify
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_query = request.form['search_query']
        theses = Thesis.query.filter(Thesis.title.ilike(f'%{search_query}%')).all()
    else:
        theses = Thesis.query.all()

    return render_template('home.html', theses=theses)

@views.route('/toggle-table', methods=['POST'])
def toggle_table():
    hide_table = request.json.get('hide_table')
    return jsonify({'hide_table': hide_table})

@views.route('/update/<int:thesis_id>', methods=['GET', 'POST'])
def update(thesis_id):
    thesis = Thesis.query.get_or_404(thesis_id)

    if request.method == 'POST':
        thesis.title = request.form['thesis_title']
        thesis.abstract = request.form['thesis_abstract']
        db.session.commit()
        flash('Thesis updated successfully')
        return redirect('/')

    return render_template('update.html', thesis=thesis)

@views.route('/delete/<int:thesis_id>', methods=['POST'])
def delete(thesis_id):
    thesis = Thesis.query.get_or_404(thesis_id)
    db.session.delete(thesis)
    db.session.commit()
    flash('Thesis deleted successfully')
    return redirect('/')

@views.route('/view-all', methods=['POST'])
def view_all():
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

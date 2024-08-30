"""
45.Explain how to use Flask-WTF to create and validate forms in a Flask application.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


from flask import Flask, render_template, redirect, url_for
from forms import MyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        # Process the form data
        return redirect(url_for('success'))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return "Form successfully submitted!"

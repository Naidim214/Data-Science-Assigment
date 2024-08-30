"""
49. Make a fully functional web application using flask, Mangodb. Signup,Signin page.And after successfully
login .Say hello Geeks message at webpage.
"""

from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'nadim'
bcrypt = Bcrypt(app)

client = MongoClient("mongodb://localhost:27017/")
db = client['user_db']
users = db['users']


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        users.insert_one({'username': username, 'password': password})
        return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username})

        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'

    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Hello, Geeks! Welcome {session['username']}"
    return redirect(url_for('signin'))

if __name__=="__main__":
    app.run()
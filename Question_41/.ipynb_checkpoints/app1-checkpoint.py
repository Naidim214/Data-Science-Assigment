"""
41.Write a Flask route that accepts a parameter in the URL and displays it on the page.
"""


from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)

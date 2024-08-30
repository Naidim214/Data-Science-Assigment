"""40.Explain how to set up a Flask application to handle form submissions using POST requests."""


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/submit">
            <input type="text" name="name" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'


if __name__=="__main__":
    app.run(debug=True)

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home_page():
    return 'this is homepage'

if __name__=="__main__":
    app.run()
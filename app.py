from flask import Flask


app = Flask(__name__)


@app.route('/')
def twtxt():
    return 'Hello, World!'

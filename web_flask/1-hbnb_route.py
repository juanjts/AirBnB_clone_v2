#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''function that display "Hello HBNB!"'''
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    '''function to display "HBNB" after /hbnb'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

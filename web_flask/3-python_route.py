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

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''funtion that display "C " + value of text = <text>'''
    return 'C {}'.format(text).replace('_', ' ')

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''funtion that display "Python" + value of text = <text>'''
    return 'Python {}'.format(text).replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

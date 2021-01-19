#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def int_number(n):
    '''funtion that display value of n + "is a number"'''
    return '{} is a number'.format(n).replace('_', ' ')


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    '''funtion that display an HTML page if n is int type'''
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    '''funtion that display an HTML page depending ofn value'''
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

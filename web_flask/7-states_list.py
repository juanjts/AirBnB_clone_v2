#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Call the storage.close() method"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a HTML page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

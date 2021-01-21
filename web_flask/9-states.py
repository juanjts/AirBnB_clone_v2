#!/usr/bin/python3
""" Start Flask Web Application """
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ display a HTML page """
    states = storage.all('State')
    if id:
        key_values = 'State.' + id
        if key_values in states:
            states = states[key_values]
        else:
            states = None
    else:
        states = states.values()
    return render_template('9-states.html',
                           states=states,
                           id=id)


@app.teardown_appcontext
def teardown_self(self):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')

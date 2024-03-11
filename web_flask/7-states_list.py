#!/usr/bin/python3
"""frigging documentation for module for dynamic routes"""
from flask import Flask, abort, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', items=all_states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

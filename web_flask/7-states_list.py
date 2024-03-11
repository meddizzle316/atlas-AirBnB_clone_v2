#!/usr/bin/python3
"""frigging documentation for module for dynamic routes"""
from flask import Flask, abort, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    pass


@app.teardown_appcontext
def teardown():
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

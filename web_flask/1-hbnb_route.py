#!/usr/bin/python3
"""module about flask app that does two routes"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route("/hbnh", strict_slashes=False)
def hbnb():
    return 'HBNB'

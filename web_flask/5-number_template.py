#!/usr/bin/python3
"""frigging documentation for module for dynamic routes"""
from flask import Flask, abort, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    safe_text = escape(text)
    safe_text = safe_text.replace("_", " ")
    return f"C {safe_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    safe_text = escape(text)
    safe_text = safe_text.replace("_", " ")
    return f"Python {safe_text}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    try:
        int_n = int(n)
        return f'{n} is a number'
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        int_n = int(n)
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

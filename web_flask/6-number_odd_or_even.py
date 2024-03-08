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
    try:
        float_n = float(n)
        if float_n % 1 == 0:
            int_n = int(float_n)
            return render_template('5-number.html', n=int_n)
        else:
            abort(404)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    try:
        float_n = float(n)
        if float_n % 1 == 0:
            int_n = int(float_n)
            if int_n % 2 == 0:
                odd_or_even = "even"
            else:
                odd_or_even = "odd"
            return render_template('6-number.html', n=int_n, odd_or_even=odd_or_even)
        else:
            abort(404)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

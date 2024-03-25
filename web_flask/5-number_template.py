#!/usr/bin/python3
"""
A script to start Flask application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    return f"""
    <!DOCTYPE html>
    <HTML lang="en">
        <HEAD>
            <TITLE>HBNB</TITLE>
        </HEAD>
        <BODY>
            <H1>Number: {n}</H1>
        </BODY>
    </HTML>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

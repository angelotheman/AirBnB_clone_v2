#!/usr/bin/python3
"""
A script to start Flask application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


@app.route("/state_list", strict_slashes=False)
def state_list():
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

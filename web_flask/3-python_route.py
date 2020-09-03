#!/usr/bin/python3

''' Ok '''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    ''' main route '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    ''' hbnb route '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    ''' C route '''
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    ''' Python Route '''
    return "Python " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def python_route2():
    ''' Python Route '''
    return "Python is cool"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

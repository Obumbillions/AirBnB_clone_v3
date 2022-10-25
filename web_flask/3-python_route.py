#!/usr/bin/python3
"""Simple Flask web application"""
from flask import Flask
app = Flask('weblo HBNB!'"""
    return 'Hello HBNB!'


@app.route_flask')
app.url_map.strict_slashes = False


@app.route('/')
def hello_route1():
    """Return 'Hel('/hbnb')
def hello_route2():
    """Return 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def hello_route3(text):
    """Return 'C ' followed by text from html request"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def hello_route4(text):
    """Return 'Python ' followed by text from html request with
    default text 'is cool'"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

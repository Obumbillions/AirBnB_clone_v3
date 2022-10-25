#!/usr/bin/python3
"""Simple Flask web applief hello_route():
    """Return simple string"""
 cation"""
from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
d   return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

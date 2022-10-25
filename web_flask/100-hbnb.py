#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template
from models import storage
app = Flask('web_flask')
app.url_map.strict_slab():
    """Generate page with popdown menu of stashes = False


@app.route('/hbnb')
def display_hbntes/cities"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = 00-hbnb.html',
                           states=sstorage.all('Place')
    return render_template('1tates,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

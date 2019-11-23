#!/usr/bin/python3
"""
Sets a Flask web application
"""
from flask import Flask, url_for, render_template
import json
import uuid


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index page
    """
    return render_template('index.html', cache_id=str(uuid.uuid4()))


@app.route('/people', methods=['GET'], strict_slashes=False)
def searchingforsomeone():
    """
    This route loads the info for a given username
    """
    return render_template('getUser.html', cache_id=str(uuid.uuid4()))

@app.route('/people/connections', methods=['GET'], strict_slashes=False)
def lookingforconnections():
    """
    This module gets all about connections of a given user
    """
    return render_template('candidatesforskills.html', cache_id=str(uuid.uuid4()))


@app.route('/people/<username>/buildateam')
def building_teams(username):
    """
    This file creates a team given some parameters from the URL route
    """
    return render_template('candidatesforskills.html', cache_id=str(uuid.uuid4()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)

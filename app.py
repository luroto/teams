#!/usr/bin/python3
from gettingdata import 

"""
Sets a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict=slashes=False)
def index():
    """
    Returns the index page
    """
    return 'Hi there! The index route is working!'


@route('/people/:username')
def sear    chingforsomeone:
    """ 
    This module gets info for a fiven username
    """
        

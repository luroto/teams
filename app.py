#!/usr/bin/python3
"""
Sets a Flask web application
"""
from flask import Flask
from functions.gettingdata import userDataSkills

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index page
    """
    return 'Hi there! The index route is working!'


@app.route('/people/<username>')
def searchingforsomeone(username):
    """ 
    This module gets info for a fiven username
    """
    public_Id = username
    usuario = userDataSkills(public_Id=username) 
    return(usuario)
 


app.run(host='0.0.0.0', port='5000')

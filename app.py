#!/usr/bin/python3
"""
Sets a Flask web application
"""
from flask import Flask, request
from functions.gettingdata import userDataSkills
import json
from models.UserData import UserData



app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns the index page
    """
    return 'Hi there! The index route is working!'


@app.route('/people/<username>', strict_slashes=False)
def searchingforsomeone(username):
    """ 
    This module gets info for a fiven username
    """
    usuario = UserData()
    to_update = userDataSkills(public_Id=username)
    usuario.update(**to_update)
    usuario = json.dumps(str(usuario), ensure_ascii=False)
    return (usuario)

@app.route('/people/<username>/connections', strict_slashes=False)
def lookingforconnections(username, path=None):
    """
    This module gets all about connections
    """
    queries = []
    for item in request.args:
        queries.append(to_dict(item))

    return(str(type(requ)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

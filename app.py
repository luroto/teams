#!/usr/bin/python3
"""
Sets a Flask web application
"""
from flask import Flask, request, Response
from functions.userDataSkills import userDataSkills
from functions.ConnectingUser import ConnectingUser
from functions.GettingSkillsforCandidates import GettingSkillsforCandidates
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
    return (Response(usuario, mimetype='application/json'))


@app.route('/people/<username>/connections', strict_slashes=False)
def lookingforconnections(username, path=None):
    """
    This module gets all about connections
    """
    returning = []
    queries = dict(request.args.items())
    if 'skill' in request.args:
        skills = list(request.args.getlist('skill'))
        queries.pop('skill')
        queries['skills'] = skills
    queries['public_Id'] = username
    candidates = ConnectingUser(**queries) 
    if 'skills' in queries:
        queries['listofcandidates'] = candidates
        return ("ratoncito")
    else:
        for candidate in candidates:
            returning.append(userDataSkills(public_Id=candidate))
        respuesta = json.dumps(returning, ensure_ascii=False)
        return Response(respuesta, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

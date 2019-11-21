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
    This module gets info for a given username
    """
    usuario = UserData()
    to_update = userDataSkills(public_Id=username)
    usuario.update(**to_update)
    usuario = json.dumps(str(usuario), ensure_ascii=False)
    return (Response(usuario, mimetype='application/json'))


@app.route('/people/<username>/connections', strict_slashes=False)
def lookingforconnections(username):
    """
    This module gets all about connections of a given user
    """
    returning = []
    queries = dict(request.args.items())
    queries['public_Id'] = username
    candidates = ConnectingUser(**queries)
    if type(candidates) is dict:
        candidates = json.dumps(candidates)
        return Response(candidates, mimetype='application/json')
    for candidate in candidates:
        returning.append(userDataSkills(public_Id=candidate))
    respuesta = json.dumps(returning, ensure_ascii=False)
    return Response(respuesta, mimetype='application/json')


@app.route('/people/<username>/buildateam')
def building_teams(username):
    """
    This file creates a team given some parameters from the URL route
    """
    queries = dict(request.args.items())
    request.args.get('skill')
    if request.args.get('skill') is None:
        message = {'message': 'You must pass at least one skill on the route'}
        message = json.dumps(message, ensure_ascii=False)
        return Response(message, mimetype='application/json')
    else:
        skills = list(request.args.getlist('skill'))
        queries.pop('skill')
        queries['skills'] = skills
        queries['public_Id'] = username
        candidates = ConnectingUser(**queries)
        queries['listofcandidates'] = candidates
        candidateswithskills = GettingSkillsforCandidates(**queries)
        return candidateswithskills


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

#!/usr/bin/python3

from api.v1.views import app_views
from flask import Response, request, make_response
import requests
import json
from functions import userDataSkills
from functions import GettingSkillsforCandidates
from functions import ConnectingUser
from models import UserTeam
from models import UserData

@app_views.route("/people/<username>", strict_slashes=False, methods=['GET'])
def searchingforsomeone(username):
    """
    This module gets info for a given username
    """
    usuario = UserData()
    to_update = userDataSkills(public_Id=username)
    usuario.update(**to_update)
    usuario = json.dumps(str(usuario), ensure_ascii=False)
    r = Response(response=usuario, status=200, mimetype="application/json")
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

@app_views.route('/people/<username>/connections', strict_slashes=False)
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


@app_views.route('/people/<username>/buildateam')
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

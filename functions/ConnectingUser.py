#!/usr/bin/python3
"""
This file handles the functions for getting data
"""
import requests
from models.UserTeam import UserTeam
from .userDataSkills import userDataSkills
from flask import jsonify

def ConnectingUser(*args, **kwargs):
    """
    This function handles with the user candidates for the team
    """
    public_Id = kwargs['public_Id']
    urlforconnections = ('https://bio.torre.co/api/people/{}/connections'.format(public_Id))
    listofcandidates = []
    if 'q'in kwargs and 'limit' in kwargs:
        urlforconnections += '?' + "q=" + kwargs.get("q") + "&" + "limit=" + kwargs.get("limit")
    elif "q" in kwargs:
        urlforconnections += '?' + "q=" + kwargs.get("q")
    elif "limit" in kwargs:
        urlforconnections += '?' + 'limit=' + kwargs.get('limit')
    try:
        user_connections = requests.get(urlforconnections)
    except user_connections.RequestException as errorcillo:
        return (errorcillo)
    if 200 <= user_connections.status_code <= 400:
        user_connections = user_connections.json()
        if 'degree' in kwargs is True:
            for candidate in user_connections:
                if candidate['degrees'] == int(kwargs['degree']):
                    listofcandidates.append(candidate['person']['publicId'])
            return listofcandidates
        else:
            for candidate in user_connections:
                listofcandidates.append(candidate['person']['publicId'])
            return listofcandidates
    else:
        return {'message': 'Username doesnt exist in Torre'}

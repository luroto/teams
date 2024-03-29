#!/usr/bin/python3
"""
This file handles the functions for getting data
"""
import requests
from models import UserData


def userDataSkills(**kwargs):
    """
    This function gets all about a username as initial member of a team
    """
    public_Id = kwargs['public_Id']
    urlforuser = "https://bio.torre.co/api/bios/" + public_Id
    try:
        user_data = requests.get(urlforuser)
    except user_data.RequestException as errorcillo:
        return(errorcillo)
    if user_data.status_code > 200 and user_data.status_code < 400:
        user_data = user_data.json()
        public_Id = user_data['person']['publicId']
        fullname = user_data['person']['name']
        professionalHeadline = user_data['person']['professionalHeadline']
        skills = []
    for strength in user_data['person']['strengths']:
        skills.append({'skill_name': strength.name,
                      'skill_code': strength.code,
                       'weight': strength.weight})
    usuario = UserData(public_Id, fullname, professionalHeadline, **skills)
    return (usuario)


def ConnectingUser(**kwargs):
    """
    This function handles with the user candidates for the team
    """
    public_Id = kwargs['public_Id']
    urlforconnections = ('https://bio.torre.co/api/people/{}/connections' +
                        public_Id)
    listofcandidates = []
    if 'q'in kwargs and 'limit' in kwargs:
        urlforconnections += "q=" + kwargs.get("q") + "&" + "limit=" +
                          kwargs.get("limit")
    elif "q" in kwargs:
        urlforconnections += "q=" + kwargs.get("q")
    elif "limit" in kwargs:
        urlforconnections += 'limit=' + kwargs.get('limit')
    try:
        user_connections = requests.get(urlforconnections)
    except user_connections.RequestException as errorcillo:
        return (errorcillo)
    if user_connections.status_code >= 200 and user_connections.status_code <= 400:
        user_connections = user_connections.json()
        for candidate in user_connections:
            listofcandidates.append(candidate['person']['publicId'])
        return listofcandidates


def GettingSkillsforCandidates(**kwargs):
    """ 
    This function handles the candidates and their skills

    """
    listofcandidates = kwargs['listofcandidates']
    final_candidate_list = []
    final_list = []
    username = kwargs['publicId']
    if kwargs['listofskills']:
        listofskills = kwargs['listofskills']
        skillsandcandidates = {}
    urlforcandidates = "https://bio.torre.co/api/bios/" 
    for candidates in listofcandidates:
        candidatebios = urlforcandidates + candidates
        candidate_data = requests.get(candidatebios)
        if candidate_data.status_code >= 200 and candidate_data.status_code <= 400:
            candidate_data = candidate_data.json()
        else:
            return candidate_data.exceptions.RequestException
        if (listofskills):
            for skill in listofskills:
                if any(d['name'] == skill for d in candidate_data['strengths']):
                    skillsandcandidates[skill] = [{"public_id": candidate_data['person']['publicId'], 
                    "name": candidate_data['person']['name'],
                    'skill': candidate_data['strengths']['name'],
                    'weight': candidate_data['strengths']['weight']}]
                    rolling = [x['weight'] for x in skillsandcandidates]
                    listofskills['max'] = max(rolling)
                    for dictio in skillsandcandidates:
                        if dictio['weight'] == listofskills['max']:
                            final_candidate_list.append({skill: dictio})
            initialUserData = userDataSkills(username)
            if (listofskills):
                initialUserData.append(listofskills)
            final_list = [initialUserData, final_candidate_list]
            return (final_list)


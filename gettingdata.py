#!/usr/bin/python3
""" 
This file handles the functions for getting data
"""
import requests 

def userDataSkills(*args):
    """
    This function gets all about a username as initial member of a team
    """ 
    urlforuser = "https://bio.torre.co/api/bios/" + publicId
    user_data = requests.get(urlforuser)
    if user_data.status_code > 200 and user_data.status_code < 400:
        user_data = user_data.json()
        public_id = user_data['person']['publicId']
        fullname = user_data['person']['name']
        professionalHeadline = user_data['person']['professionalHeadline']
        skills = []
        for strength in user_data['person']['strengths']:
            skills.append({'skill_name': strength.name, 'skill_code': strength.code, 'weight': strength.weight})
        usuario = UserData(public_id, fullname, professionalHeadline, **skills)
        return (usuario)

def ConnectingUser(**kwargs):
    """
    This function handles with the user candidates for the team
    """ 
    urlforconnections = ('https://bio.torre.co/api/people/{}/connections'.format(publicId))
    listofcandidates = []
    if 'q'in kwargs and 'limit' in kwargs:
        urlforconnections += "q=" + kwargs.get("q") + "&" + "limit=" +kwargs.get("limit")
    elif "q" in kwargs:
        urlconnections += "q=" + kwargs.get("q")
    elif "limit" in kwargs:i
        urlconnections += 'limit=' + kwargs.get('limit')
    user_connections = requests.get(urlconnections)
    if user_connections.status_code >= 200 and user_connections.status_code <= 400:
        user_connections = user_connections.json()
        for candidate in user_connections:
            listofcandidates.append(candidate['person']['publicId'])
        return listofcandidates

def GettingSkillsforCandidates(**kwargs)
    """ 
    This function handles the candidates and their skills

    """
    listofcandidates = kwargs['listofcandidates']
    if kwargs['listofskills']:
        listofskills = kwargs['listofskills']
        skillsandcandidates = {}
    urlforcandidates = "https://bio.torre.co/api/bios/" 
    for candidates in listofcandidates:
        candidatebios = urlforcandidates += candidates
        candidate_data = requests.get(candidatebios)
        if candidate_data.status_code >= 200 and candidate_data.status_code <= 400:
            candidate_data = candidate_data.json()
            if (listofskills):
            for skill in listofskills:
                if any(d['name'] == skill for d in candidate_data['strengths']):
                    skillsandcandidates[skill] = [{"public_id": candidate_data['person']['publicId'], "name": candidate_date['person']['name'], 'skill': candidate_data['strengths']['name'], 'weight': candidate['strengths']['weight']}]

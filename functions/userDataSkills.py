#!/usr/bin/python3
"""
This file handles the functions for getting data
"""
import requests
from flask import jsonify


def userDataSkills(**dictionary):
    """
    This function gets all about a username as initial member of a team
    """
    public_Id = dictionary['public_Id']
    urlforuser = "https://bio.torre.co/api/bios/" + public_Id
    fullname = ""
    professionalHeadline = ""
    skills = []
    photo_url = ""
    user_data = requests
    try:
        user_data = requests.get(urlforuser)
        user_data.encoding = 'utf-8'
    except user_data.RequestException as errorcillo:
        return(errorcillo)
    print (user_data.status_code)
    if user_data.status_code >= 200 and user_data.status_code <= 400:
        user_data = user_data.json()
        public_Id = user_data['person']['publicId']
        fullname = user_data['person']['name']
        professionalHeadline = user_data['person']['professionalHeadline']
        if 'picture' in user_data['person']:
            photo_url = user_data['person']['picture']
        skills = []
        for strength in user_data['strengths']:
            skills.append({'skill_name': strength['name'],
                          'skill_code': strength['code'],
                           'weight': strength['weight']})
        dictio = {'public_Id': public_Id,
                  'fullname': fullname,
                  'professionalHeadline': professionalHeadline,
                  'skills': skills}
        if photo_url != "":
            dictio['photo_url'] = photo_url
        return (dictio)

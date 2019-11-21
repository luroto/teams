#!/usr/bin/python3
"""
This function handles when user searchs a skills in connections
"""
from .userDataSkills import userDataSkills
def GettingSkillsforCandidates(*args, **kwargs):
    """
    This function handles the candidates and their skills

    """
    listofcandidates = kwargs['listofcandidates']
    final_dictio = {} 
    username = kwargs['public_Id']
    listofskills = kwargs['skills']
    candidatesforchecking = []
    gettingweight = []
    skillsandcandidates = {}
    for skill in listofskills:
        skillsandcandidates[skill] = []
    for candidates in listofcandidates:
        candidatesforchecking.append(userDataSkills(public_Id=candidates))
    for skill in listofskills:
        for candidate_data in candidatesforchecking:
            if any(d['skill_name'] == skill for d in candidate_data['skills']):
                skillsandcandidates[skill].append(candidate_data)
        for candidate in skillsandcandidates[skill]:
            for checking in candidate['skills']:
                if checking['skill_name'] == skill:
                    gettingweight.append(checking['weight'])
        maxbyskill = max(gettingweight)
        final_dictio[skill] = skillsandcandidates[skill][gettingweight.index(maxbyskill)]
    print(final_dictio)
    return (final_dictio)

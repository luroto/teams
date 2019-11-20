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
    final_candidate_list = []
    final_list = []
    username = kwargs['public_Id']
    listofskills = kwargs['skills']
    candidatesforchecking = []
    skillsandcandidates = {}
    for skill in listofskills:
        skillsandcandidates[skill] = []
    for candidates in listofcandidates:
        candidatesforchecking.append(userDataSkills(public_Id=candidates))
    for skill in listofskills:
        for candidate_data in candidatesforchecking:
            if any(d['skill_name'] == skill for d in candidate_data['skills']):
                skillsandcandidates[skill].append(candidate_data)
    print (skillsandcandidates)
    return (final_list)

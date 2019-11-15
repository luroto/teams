def GettingSkillsforCandidates(*args, **kwargs):
    """
    This function handles the candidates and their skills

    """
    listofcandidates = kwargs['listofcandidates']
    final_candidate_list = []
    final_list = []
    username = kwargs['publicId']
    if kwargs['skills']:
        listofskills = kwargs['skills']
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

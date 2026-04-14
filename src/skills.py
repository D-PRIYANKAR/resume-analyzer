def extract_skills(text, skills_list):
    found = []
    text = text.lower()

    for skill in skills_list:
        if skill.lower() in text:
            found.append(skill)

    return found
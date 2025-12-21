def normalize(value):
    mapping = {
        "Low": 3,
        "Medium": 6,
        "High": 9
    }
    return mapping.get(value, value)


def get_student_profile(interest, skill, risk, finance, grind, stability):
    return {
        "interest": interest,
        "skill": skill,
        "risk": normalize(risk),
        "finance": normalize(finance),
        "grind": normalize(grind),
        "stability": normalize(stability)
    }

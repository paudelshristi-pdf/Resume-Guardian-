from clean_text import clean_text
from extract_skills import extract_skills
from semantic_match import semantic_score, read_file

SEMANTIC_WEIGHT = 0.6
SKILL_WEIGHT = 0.4


def rescale(score, low=0.1, high=0.6):
    scaled = (score - low) / (high - low)
    return max(0.0, min(1.0, scaled))


def match_resume_to_job(resume_text, jd_text):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))
    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    semantic = rescale(semantic_score(resume_text, jd_text))

    if jd_skills:
        skill_score = len(matched) / len(jd_skills)
        final = SEMANTIC_WEIGHT * semantic + SKILL_WEIGHT * skill_score
    else:
        skill_score = None
        final = semantic

    return {
        "final_score": round(final * 100),
        "semantic_score": round(semantic * 100),
        "skill_score": None if skill_score is None else round(skill_score * 100),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
    }


if __name__ == "__main__":
    resume_text = clean_text(read_file("data/resumes_text/R1.txt"))
    jd_text = clean_text(read_file("data/job_descriptions/jd_Agentic AI Engineer.txt"))

    result = match_resume_to_job(resume_text, jd_text)
    for key, value in result.items():
        print(f"{key}: {value}")
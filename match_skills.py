from clean_text import clean_text
from extract_skills import extract_skills

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


resume_text = clean_text(read_file("data/resumes_text/test_ai_resume.txt"))
jd_text = clean_text(read_file("data/job_descriptions/jd_Agentic AI Engineer.txt"))

resume_skills = set(extract_skills(resume_text))
jd_skills = set(extract_skills(jd_text))

matched = resume_skills & jd_skills
missing = jd_skills - resume_skills

print("Resume skills:", sorted(resume_skills))
print("Job Description skills:", sorted(jd_skills))
print()
print("Matched skills:", sorted(matched))
print("Missing skills:", sorted(missing))
if jd_skills:
    percent = len(matched) / len(jd_skills) * 100
    print(f"Skill match percentage: {percent:.0f}%")
else:
    print("No skills found in the job description.")

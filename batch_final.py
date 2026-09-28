import os
from clean_text import clean_text
from semantic_match import read_file
from final_score import match_resume_to_job

resume_folder = "data/resumes_text"
jd_folder = "data/job_descriptions"


def load_folder(folder):
    texts = {}
    for name in os.listdir(folder):
        if name.endswith(".txt"):
            texts[name] = clean_text(read_file(os.path.join(folder, name)))
    return texts


resumes = load_folder(resume_folder)
jds = load_folder(jd_folder)

print(f"{'resume':<10}{'job':<38}{'final':>6}{'sem':>6}{'skill':>7}")
for r_name, r_text in resumes.items():
    for j_name, j_text in jds.items():
        result = match_resume_to_job(r_text, j_text)
        print(
            f"{r_name[:8]:<10}{j_name[:36]:<38}"
            f"{result['final_score']:>6}{result['semantic_score']:>6}"
            f"{str(result['skill_score']):>7}"
        )
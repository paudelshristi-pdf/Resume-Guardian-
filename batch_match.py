import os
from clean_text import clean_text
from semantic_match import semantic_score, read_file

resume_folder = "data/resumes_text"
jd_folder = "data/job_descriptions"

resumes = {}
for name in os.listdir(resume_folder):
    if name.endswith(".txt"):
        resumes[name] = clean_text(read_file(os.path.join(resume_folder, name)))

jds = {}
for name in os.listdir(jd_folder):
    if name.endswith(".txt"):
        jds[name] = clean_text(read_file(os.path.join(jd_folder, name)))

print(f"{'resume':<22}{'job':<40}{'raw':>6}")
for r_name, r_text in resumes.items():
    for j_name, j_text in jds.items():
        raw = semantic_score(r_text, j_text)
        print(f"{r_name[:20]:<22}{j_name[:38]:<40}{raw:>6.3f}")
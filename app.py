import streamlit as st

from extract_text import PdfReader
from clean_text import clean_text
from final_score import match_resume_to_job

st.title("Resume Guardian")
st.write("Upload your resume and paste a job description to see how well they match.")


def read_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


resume_file = st.file_uploader("Resume (PDF)", type=["pdf"])
job_description = st.text_area("Job description", height=250)

if st.button("Analyze"):
    if resume_file is None or not job_description.strip():
        st.warning("Please upload a resume and fill in the job description.")
    else:
        with st.spinner("Analyzing..."):
            resume_text = clean_text(read_pdf(resume_file))
            jd_text = clean_text(job_description)
            result = match_resume_to_job(resume_text, jd_text)

        st.metric("Overall match", f"{result['final_score']}%")
        st.write("Matched skills:", ", ".join(result["matched_skills"]) or "none")
        st.write("Missing skills:", ", ".join(result["missing_skills"]) or "none")
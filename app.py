import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/match"

st.title("Resume Guardian")
st.write("Paste your resume and a job description to see how well they match.")

resume_text = st.text_area("Resume", height=250)
job_description = st.text_area("Job description", height=250)

if st.button("Analyze"):
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please fill in both boxes.")
    else:
        response = requests.post(
            API_URL,
            json={"resume_text": resume_text, "job_description": job_description},
        )
        result = response.json()

        st.metric("Overall match", f"{result['final_score']}%")
        st.write("Matched skills:", ", ".join(result["matched_skills"]) or "none")
        st.write("Missing skills:", ", ".join(result["missing_skills"]) or "none")
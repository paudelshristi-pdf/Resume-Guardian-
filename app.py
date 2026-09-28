import requests
import streamlit as st

from extract_text import PdfReader  # reuse the PDF-reading tool you already built

API_URL = "http://127.0.0.1:8000/match"

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
        resume_text = read_pdf(resume_file)

        try:
            response = requests.post(
                API_URL,
                json={"resume_text": resume_text, "job_description": job_description},
                timeout=15,
            )
            response.raise_for_status()
            result = response.json()

        except requests.exceptions.ConnectionError:
            st.error(
                "Can't reach the matching service. Make sure the API "
                "(uvicorn) is running in another terminal, then try again."
            )
        except requests.exceptions.Timeout:
            st.error("The matching service took too long to respond. Try again.")
        except requests.exceptions.HTTPError:
            st.error(f"The matching service returned an error: {response.status_code}")
        else:
            st.metric("Overall match", f"{result['final_score']}%")
            st.write("Matched skills:", ", ".join(result["matched_skills"]) or "none")
            st.write("Missing skills:", ", ".join(result["missing_skills"]) or "none")
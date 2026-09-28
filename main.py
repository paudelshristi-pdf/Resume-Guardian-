from fastapi import FastAPI
from pydantic import BaseModel

from clean_text import clean_text
from final_score import match_resume_to_job

app = FastAPI(title="Resume Guardian")


class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def home():
    return {"message": "Resume Guardian API is running"}


@app.post("/match")
def match(request: MatchRequest):
    resume = clean_text(request.resume_text)
    jd = clean_text(request.job_description)
    return match_resume_to_job(resume, jd)
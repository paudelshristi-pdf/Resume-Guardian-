import spacy
from spacy.matcher import PhraseMatcher
from skills import SKILLS
from clean_text import clean_text

nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILLS]
matcher.add("SKILLS", patterns)


def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)
    found = set()
    for match_id, start, end in matches:
        found.add(doc[start:end].text.lower())
    return sorted(found)


if __name__ == "__main__":
    with open("data/resumes_text/R1.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    cleaned = clean_text(raw)
    print(extract_skills(cleaned))
import spacy
from spacy.matcher import PhraseMatcher
from skills import SKILLS, ALIASES
from clean_text import clean_text

nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
all_terms = SKILLS + list(ALIASES.keys())
patterns = [nlp.make_doc(term) for term in all_terms]
matcher.add("SKILLS", patterns)


def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)
    found = set()
    for match_id, start, end in matches:
        term = doc[start:end].text.lower()
        found.add(ALIASES.get(term, term))
    return sorted(found)


if __name__ == "__main__":
    with open("data/resumes_text/R1.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    print(extract_skills(clean_text(raw)))
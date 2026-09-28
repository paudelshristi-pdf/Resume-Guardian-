import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from clean_text import clean_text

model = SentenceTransformer("all-MiniLM-L6-v2")


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def chunk_text(text, size=150):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size):
        chunk = " ".join(words[i:i + size])
        chunks.append(chunk)
    return chunks


def embed_document(text):
    chunks = chunk_text(text)
    vectors = model.encode(chunks)
    return np.mean(vectors, axis=0)


def semantic_score(resume_text, jd_text):
    resume_vec = embed_document(resume_text)
    jd_vec = embed_document(jd_text)
    return cos_sim(resume_vec, jd_vec).item()

if __name__ == "__main__":
    resume_text = clean_text(read_file("data/resumes_text/R1.txt"))
    jd_text = clean_text(read_file("data/job_descriptions/jd_Agentic AI Engineer.txt"))
    unrelated = "Seeking a pastry chef to bake bread, cakes, and croissants in a busy bakery. Must work early mornings and manage inventory."

    print("Resume chunks:", len(chunk_text(resume_text)))
    print("JD chunks:", len(chunk_text(jd_text)))

    old_score = cos_sim(model.encode(resume_text), model.encode(jd_text)).item()
    new_score = semantic_score(resume_text, jd_text)
    bakery_score = semantic_score(resume_text, unrelated)

    print(f"Old score (first ~200 words only): {old_score:.3f}")
    print(f"New score (whole document):        {new_score:.3f}")
    print(f"Resume vs unrelated bakery job:    {bakery_score:.3f}")
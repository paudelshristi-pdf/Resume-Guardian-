from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Managed Windows servers and Active Directory for a large company",
    "Experience administering enterprise IT infrastructure",
    "Baked sourdough bread with a wild yeast starter",
]

embeddings = model.encode(sentences)

print("Shape:", embeddings.shape)
print("Sentence 1 vs 2:", cos_sim(embeddings[0], embeddings[1]).item())
print("Sentence 1 vs 3:", cos_sim(embeddings[0], embeddings[2]).item())
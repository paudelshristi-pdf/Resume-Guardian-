import re

def clean_text(text):
    # 1. Remove weird non-ASCII characters (like ï¼)
    text = text.encode("ascii", "ignore").decode("ascii")

    # 2. Replace all whitespace runs (spaces, tabs, newlines) with a single space
    text = re.sub(r"\s+", " ", text)

    # 3. Remove leading/trailing spaces
    text = text.strip()

    return text


if __name__ == "__main__":
    with open("data/resumes_text/R1.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    cleaned = clean_text(raw)
    print(cleaned[:500])
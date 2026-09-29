from pypdf import PdfReader
import os


def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


if __name__ == "__main__":
    resume_folder = "data/resumes"
    output_folder = "data/resumes_text"

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(resume_folder, filename)
            text = extract_text_from_pdf(filepath)

            output_name = filename.replace(".pdf", ".txt")
            output_path = os.path.join(output_folder, output_name)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Saved {output_name} ({len(text)} characters)")
import fitz
import re
from docx import Document


# Extract PDF Text
def extract_pdf(file_path):

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    return text


# Extract DOCX Text
def extract_docx(file_path):

    doc = Document(file_path)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)


# Main Resume Extraction
def extract_resume(file_path):

    if file_path.endswith(".pdf"):
        return extract_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_docx(file_path)

    else:
        return "Unsupported file format"


# Clean & Normalize Text
def clean_resume_text(text):
    cleaned_lines = []

    for line in text.splitlines():
        line = " ".join(line.split())   # collapse spaces within the line
        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


# Save Output
def save_output(text, output_path):

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
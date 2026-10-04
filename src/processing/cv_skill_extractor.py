from src.processing.cv_extractor import extract_cv_text
from src.extractor.regex_extractor import extract_skills

def extract_cv_skills(pdf_path: str) -> list[str]:
    text = extract_cv_text(pdf_path)

    if not text.strip():
        return []

    return extract_skills(text)
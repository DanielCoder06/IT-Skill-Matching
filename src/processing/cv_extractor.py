from pathlib import Path
from src.processing.cv_text_extractor import extract_text_from_pdf
from src.processing.cv_ocr import extract_text_with_ocr

# Minimum length of text to be considered for CV extraction
MIN_TEXT_LENGTH = 200

def extract_cv_text(pdf_path: str | Path) -> str:
    """
    Extract text from a CV PDF.
        1. Try PyMuPDF first.
        2. If extracted text is too short, use OCR.
    """
    text = extract_text_from_pdf(pdf_path)
    
    if len(text.strip()) >= MIN_TEXT_LENGTH:
        return text.strip()
    
    return extract_text_with_ocr(pdf_path).strip()
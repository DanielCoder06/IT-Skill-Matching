from pathlib import Path

import pymupdf

def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extract text from all pages of a PDF file.
    """
    pdf_path = Path(pdf_path)
    document = pymupdf.open(pdf_path)
    pages_text = []
    
    for page in document:
        text = page.get_text("text")
        pages_text.append(text)
    
    document.close()
    return "\n".join(pages_text)
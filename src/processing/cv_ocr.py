from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image

def extract_text_with_ocr(
    pdf_path: str | Path, 
    language: str = "eng",
) -> str:
    """
    Extract text from a PDF using OCR.
    """
    
    pdf_path = Path(pdf_path)

    document = pymupdf.open(pdf_path)

    pages_text = []

    try:
        for page in document:
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))

            image = Image.frombytes(
                "RGB",
                [pixmap.width, pixmap.height],
                pixmap.samples,
            )

            text = pytesseract.image_to_string(
                image,
                lang=language,
            )

            pages_text.append(text)

    finally:
        document.close()

    return "\n".join(pages_text)
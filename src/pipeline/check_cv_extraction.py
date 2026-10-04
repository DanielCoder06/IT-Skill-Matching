from pathlib import Path
from src.processing.cv_extractor import extract_cv_text

PDF_DIR = Path("data/external/resumes/ResumesPDF")


def main() -> None:
    pdf_files = list(PDF_DIR.glob("*.pdf"))

    total = len(pdf_files)
    success = 0
    empty = 0
    failed = 0
    
    for pdf_path in pdf_files:
        try:
            text = extract_cv_text(pdf_path)

            if text.strip():
                success += 1
            else:
                empty += 1

        except Exception as e:
            failed += 1
            print(f"Failed: {pdf_path.name} | {e}")

    print("\n=== CV EXTRACTION RESULT ===")
    print(f"Total PDFs: {total}")
    print(f"Text extracted: {success}")
    print(f"Empty: {empty}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
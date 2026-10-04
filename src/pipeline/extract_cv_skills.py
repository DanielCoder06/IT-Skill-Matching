from pathlib import Path

from src.processing.cv_extractor import extract_cv_text
from src.processing.cv_skill_extractor import extract_cv_skills


PDF_DIR = Path("data/external/resumes/ResumesPDF")


def main() -> None:
    pdf_files = list(PDF_DIR.glob("*.pdf"))

    total = len(pdf_files)
    text_extracted = 0
    with_skills = 0
    without_skills = 0
    failed = 0
    total_skills = 0

    for pdf_path in pdf_files:
        try:
            text = extract_cv_text(pdf_path)

            if text.strip():
                text_extracted += 1

            skills = extract_cv_skills(str(pdf_path))

            if skills:
                with_skills += 1
                total_skills += len(skills)
            else:
                without_skills += 1

        except Exception as e:
            failed += 1
            print(f"Failed: {pdf_path.name} | {e}")

    print("\n=== CV SKILL EXTRACTION ===")
    print(f"Total PDFs: {total}")
    print(f"Text extracted: {text_extracted}")
    print(f"CVs with skills: {with_skills}")
    print(f"CVs without skills: {without_skills}")
    print(f"Total skills detected: {total_skills}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
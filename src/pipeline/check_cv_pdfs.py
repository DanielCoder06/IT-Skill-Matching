from pathlib import Path

import pymupdf


PDF_DIR = Path("data/external/resumes/ResumesPDF")


def main() -> None:
    pdf_files = list(PDF_DIR.glob("*.pdf"))

    total = len(pdf_files)
    success = 0
    empty = 0
    short = 0
    failed = 0

    character_counts = []

    for pdf_path in pdf_files:
        document = None

        try:
            document = pymupdf.open(pdf_path)

            text = ""

            for page in document:
                text += page.get_text("text")

            char_count = len(text.strip())

            character_counts.append(char_count)

            if char_count == 0:
                empty += 1
            elif char_count < 200:
                short += 1
            else:
                success += 1

        except Exception as e:
            failed += 1
            print(f"Failed: {pdf_path.name} | {e}")

        finally:
            if document is not None:
                document.close()

    print("\n=== CV PDF STATISTICS ===")
    print(f"Total PDFs: {total}")
    print(f"Text extracted successfully: {success}")
    print(f"Very short text (<200 chars): {short}")
    print(f"Empty text: {empty}")
    print(f"Failed PDFs: {failed}")

    if character_counts:
        print(f"Minimum characters: {min(character_counts)}")
        print(f"Maximum characters: {max(character_counts)}")
        print(
            f"Average characters: "
            f"{sum(character_counts) / len(character_counts):.2f}"
        )


if __name__ == "__main__":
    main()
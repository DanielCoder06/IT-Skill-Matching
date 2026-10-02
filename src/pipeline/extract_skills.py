import json
from pathlib import Path

from src.extractor.regex_extractor import extract_skills


INPUT_PATH = Path("data/filtered_it_jobs.json")


def main():
    with INPUT_PATH.open("r", encoding="utf-8") as f:
        jobs = json.load(f)

    total_skills = 0

    for job in jobs:
        skills = extract_skills(job["description"])
        job["skills"] = skills
        total_skills += len(skills)

    with INPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(
            jobs,
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(f"Jobs processed: {len(jobs)}")
    print(f"Skills extracted: {total_skills}")

    for job in jobs[:10]:
        print(f"\n[{job['company']}] {job['title']}")
        print("Skills:", ", ".join(job["skills"]) or "None")


if __name__ == "__main__":
    main()

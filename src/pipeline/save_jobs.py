import json
from dataclasses import asdict
from pathlib import Path

from src.sources.arbeitnow import ArbeitnowScraper
from src.sources.jobicy import JobicyScraper
from src.processing.job_adapter import raw_jobs_to_job_records
from src.processing.job_filter import filter_it_jobs


OUTPUT_PATH = Path("data/filtered_it_jobs.json")


def main():
    raw_jobs = (
        ArbeitnowScraper().fetch()
        + JobicyScraper().fetch()
    )

    jobs = raw_jobs_to_job_records(raw_jobs)
    it_jobs = filter_it_jobs(jobs)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(
            [asdict(job) for job in it_jobs],
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(f"Raw jobs: {len(raw_jobs)}")
    print(f"IT jobs: {len(it_jobs)}")
    print(f"Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

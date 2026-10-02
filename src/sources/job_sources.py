from src.sources.arbeitnow import ArbeitnowScraper
from src.sources.jobicy import JobicyScraper


def fetch_all_jobs():
    arbeitnow_jobs = ArbeitnowScraper().fetch()
    jobicy_jobs = JobicyScraper().fetch()

    return arbeitnow_jobs + jobicy_jobs


if __name__ == "__main__":
    jobs = fetch_all_jobs()

    print(f"Tổng số jobs: {len(jobs)}")

    for job in jobs[:5]:
        print(
            f"[{job.source}] "
            f"{job.title} - "
            f"{job.company}"
        )
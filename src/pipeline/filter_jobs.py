from src.sources.arbeitnow import ArbeitnowScraper
from src.sources.jobicy import JobicyScraper
from src.processing.job_adapter import raw_jobs_to_job_records
from src.processing.job_filter import filter_it_jobs


def main():
    raw_jobs = (
        ArbeitnowScraper().fetch()
        + JobicyScraper().fetch()
    )

    jobs = raw_jobs_to_job_records(raw_jobs)

    it_jobs = filter_it_jobs(jobs)

    print(f"Raw jobs: {len(raw_jobs)}")
    print(f"IT jobs: {len(it_jobs)}")

    for idx, job in enumerate(it_jobs, start=1):
        print(
            f"{idx}.[{job.company}]"
            f"{job.title}"
        )


if __name__ == "__main__":
    main()
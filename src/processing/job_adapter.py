from src.models.raw_job import RawJob
from src.models.job import JobRecord


def raw_job_to_job_record(job: RawJob) -> JobRecord:
    return JobRecord(
        title=job.title,
        company=job.company or "Unknown",
        description=job.description,
        location=job.location or "Unknown",
        url=job.job_url,
        experience=job.experience or "",
    )


def raw_jobs_to_job_records(
    jobs: list[RawJob],
) -> list[JobRecord]:
    return [
        raw_job_to_job_record(job)
        for job in jobs
    ]

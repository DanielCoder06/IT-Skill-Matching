from database.job_repository import (
    get_job_by_url,
    upsert_job,
)
from src.models.raw_job import RawJob


def test_upsert_and_get_job():
    job = RawJob(
        source="itviec",
        external_id="test-001",
        title="Python Backend Intern",
        company="Test Company",
        location="Can Tho",
        description="Python, FastAPI, PostgreSQL",
        job_url="https://example.com/jobs/test-001",
    )

    job_id = upsert_job(job)

    assert job_id is not None

    saved_job = get_job_by_url(job.job_url)

    assert saved_job is not None
    assert saved_job.title == "Python Backend Intern"
    assert saved_job.company == "Test Company"


def test_upsert_updates_existing_job():
    job = RawJob(
        source="itviec",
        external_id="test-001",
        title="Python Backend Intern",
        company="Test Company",
        location="Can Tho",
        description="Python, FastAPI, PostgreSQL",
        job_url="https://example.com/jobs/test-001",
    )

    original_id = upsert_job(job)

    updated_job = RawJob(
        source="itviec",
        external_id="test-001",
        title="Python Backend Engineer",
        company="Updated Company",
        location="Can Tho",
        description="Python, FastAPI, PostgreSQL, Docker",
        job_url="https://example.com/jobs/test-001",
    )

    updated_id = upsert_job(updated_job)

    saved_job = get_job_by_url(updated_job.job_url)

    assert updated_id == original_id
    assert saved_job is not None
    assert saved_job.title == "Python Backend Engineer"
    assert saved_job.company == "Updated Company"

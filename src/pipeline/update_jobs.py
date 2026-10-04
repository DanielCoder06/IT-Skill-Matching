from src.sources.arbeitnow import ArbeitnowScraper
from src.sources.jobicy import JobicyScraper

from src.processing.job_adapter import raw_jobs_to_job_records
from src.processing.job_filter import filter_it_jobs

from database.job_repository import upsert_job

def main():    
    # Crawl data from sources
    raw_jobs = (
        ArbeitnowScraper().fetch()
        + JobicyScraper().fetch()
    )
    
    # Convert raw jobs to job record 
    job_records = raw_jobs_to_job_records(raw_jobs)
    
    # Filter IT jobs
    it_jobs = filter_it_jobs(job_records)

    print(f"Raw jobs: {len(raw_jobs)}")
    print(f"IT jobs: {len(it_jobs)}")
    
    # Get urls of IT jobs (!set() ->delete duplicates url)
    it_job_urls = {
        job.url 
        for job in it_jobs
    }
    
    # Get raw job by url
    it_raw_jobs = [
        job
        for job in raw_jobs
        if job.job_url in it_job_urls 
    ]
    
    # Save / Update db
    saved_jobs = 0
    
    for job in it_raw_jobs:
        upsert_job(job)
        saved_jobs += 1

    print(f"Jobs saved: {saved_jobs}")
    
if __name__ == "__main__":
    main()
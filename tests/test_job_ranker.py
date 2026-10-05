from src.matching.job_ranker import calculate_match_score
from src.matching.job_ranker import (
    calculate_match_score,
    rank_jobs,
)


def test_calculate_match_score():
    result = calculate_match_score(
        matched=[
            "Python",
            "React",
            "PostgreSQL",
        ],
        job_skills=[
            "Python",
            "React",
            "PostgreSQL",
            "Docker",
        ],
        semantic_matches=[
            {
                "cv_skill": "ReactJS",
                "job_skill": "React",
                "similarity": 0.8904,
            },
            {
                "cv_skill": "Postgres",
                "job_skill": "PostgreSQL",
                "similarity": 0.8989,
            },
        ],
    )

    assert result["exact_score"] == 0.75
    assert result["semantic_score"] > 0.89
    assert result["overall_score"] > 0.79
    
def test_rank_jobs():
    jobs = [
        {
            "job_id": 1,
            "overall_score": 0.65,
        },
        {
            "job_id": 2,
            "overall_score": 0.91,
        },
        {
            "job_id": 3,
            "overall_score": 0.78,
        },
    ]

    ranked = rank_jobs(jobs)

    assert [job["job_id"] for job in ranked] == [
        2,
        3,
        1,
    ]
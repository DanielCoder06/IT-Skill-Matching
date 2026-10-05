from src.matching.recommendation import recommend_jobs


def test_recommend_jobs():
    cv_skills = [
        "Python",
        "ReactJS",
        "Postgres",
    ]

    jobs = [
        {
            "job_id": 1,
            "title": "Python Developer",
            "skills": [
                "Python",
                "React",
                "PostgreSQL",
                "Docker",
            ],
        },
        {
            "job_id": 2,
            "title": "Java Developer",
            "skills": [
                "Java",
                "Docker",
                "Kubernetes",
            ],
        },
        {
            "job_id": 3,
            "title": "Frontend Developer",
            "skills": [
                "React",
                "JavaScript",
                "CSS",
            ],
        },
    ]

    results = recommend_jobs(
        cv_skills,
        jobs,
    )

    assert len(results) == 3

    assert results[0]["job_id"] == 1

    assert (
        results[0]["overall_score"]
        >= results[1]["overall_score"]
    )

    assert (
        results[1]["overall_score"]
        >= results[2]["overall_score"]
    )
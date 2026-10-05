from src.processing.skill_matcher import hybrid_skill_match


TEST_CASES = [
    {
        "name": "Strong Python match",
        "cv": ["Python", "SQL", "Git", "Docker"],
        "job": ["Python", "SQL", "Git"],
        "expected_coverage": 1.0,
    },
    {
        "name": "Partial match",
        "cv": ["Python", "ReactJS", "Postgres"],
        "job": ["Python", "React", "PostgreSQL", "Docker"],
        "expected_coverage": 0.75,
    },
    {
        "name": "Weak match",
        "cv": ["HTML", "CSS"],
        "job": ["Python", "Docker", "SQL"],
        "expected_coverage": 0.0,
    },
]


def test_cv_job_hybrid_matching():
    print("\n=== CV JOB HYBRID MATCHING ===")

    for case in TEST_CASES:
        result = hybrid_skill_match(
            case["cv"],
            case["job"],
        )

        print(f"\n{case['name']}")
        print("CV:", case["cv"])
        print("Job:", case["job"])
        print("Matched:", result["matched"])
        print("Missing:", result["missing"])
        print("Semantic:", result["semantic_matches"])
        print("Coverage:", result["coverage"])

        assert result["coverage"] == case["expected_coverage"]
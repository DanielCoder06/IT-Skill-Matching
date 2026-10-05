SEMANTIC_THRESHOLD = 0.5

EXACT_WEIGHT = 0.7
SEMANTIC_WEIGHT = 0.3


def calculate_match_score(
    matched: list[str],
    job_skills: list[str],
    semantic_matches: list[dict],
) -> dict:
    total_job_skills = len(job_skills)

    exact_score = (
        len(matched) / total_job_skills
        if total_job_skills
        else 0.0
    )

    valid_semantic_matches = [
        match
        for match in semantic_matches
        if match["similarity"] >= SEMANTIC_THRESHOLD
    ]

    semantic_score = (
        sum(
            match["similarity"]
            for match in valid_semantic_matches
        )
        / len(valid_semantic_matches)
        if valid_semantic_matches
        else 0.0
    )

    overall_score = (
        EXACT_WEIGHT * exact_score
        + SEMANTIC_WEIGHT * semantic_score
    )

    return {
        "exact_score": exact_score,
        "semantic_score": semantic_score,
        "overall_score": overall_score,
        "semantic_matches": valid_semantic_matches,
    }
    
def rank_jobs(
    job_results: list[dict],
) -> list[dict]:
    return sorted(
        job_results,
        key=lambda job: job["overall_score"],
        reverse=True,
    )
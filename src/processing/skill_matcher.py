from sentence_transformers import util

from src.processing.skill_embedding_store import get_skill_embedding

SEMANTIC_THRESHOLD = 0.5

def exact_skill_match(
    cv_skills: list[str],
    job_skills: list[str],
) -> dict:
    cv_set = set(cv_skills)
    job_set = set(job_skills)

    matched = cv_set & job_set
    missing = job_set - cv_set

    coverage = (
        len(matched) / len(job_set)
        if job_set
        else 0.0
    )

    return {
        "matched": sorted(matched),
        "missing": sorted(missing),
        "coverage": coverage,
    }
    
def semantic_skill_match(
    cv_skills: list[str],
    job_skills: list[str],
) -> list[dict]:
    results = []

    cv_set = set(cv_skills)
    job_set = set(job_skills)

    unmatched_cv = cv_set - job_set
    unmatched_job = job_set - cv_set

    cv_vectors = {
        skill: get_skill_embedding(skill)
        for skill in unmatched_cv
    }
    job_vectors = {
        skill: get_skill_embedding(skill)
        for skill in unmatched_job
    }
    
    for cv_skill , cv_vector in cv_vectors.items():
        for job_skill, job_vector in job_vectors.items():
            similarity = util.cos_sim(
                cv_vector,
                job_vector,
            ).item()

            results.append(
                {
                    "cv_skill": cv_skill,
                    "job_skill": job_skill,
                    "similarity": similarity,
                }
            )

    return sorted(
        results,
        key=lambda x: x["similarity"],
        reverse=True,
    )
    
def hybrid_skill_match(
    cv_skills: list[str],
    job_skills: list[str],
    threshold: float = SEMANTIC_THRESHOLD,
) -> dict:
    exact_result = exact_skill_match(
        cv_skills,
        job_skills,
    )
    
    matched = set(exact_result["matched"])
    missing = set(exact_result["missing"])

    semantic_matches = []
    semantic_results = semantic_skill_match(
        cv_skills,
        job_skills,
    )
    
    matched_job_skills = set()

    for result in semantic_results:
        job_skill = result["job_skill"]

        if (
            result["similarity"] >= threshold
            and job_skill in missing
            and job_skill not in matched_job_skills
        ):
            semantic_matches.append(result)

            matched_job_skills.add(job_skill)
            matched.add(job_skill)
            missing.remove(job_skill)

    coverage = (
        len(matched) / len(job_skills)
        if job_skills
        else 0.0
    )

    return {
        "matched": sorted(matched),
        "missing": sorted(missing),
        "semantic_matches": semantic_matches,
        "coverage": coverage,
    }
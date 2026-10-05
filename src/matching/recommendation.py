from src.matching.job_ranker import calculate_match_score, rank_jobs
from src.processing.skill_matcher import (
    exact_skill_match,
    semantic_skill_match,
)


def recommend_jobs(
    cv_skills: list[str],
    jobs: list[str],
) -> list[dict]:
    results = []
    
    for job in jobs:
        job_skills = job["skills"]
        
        exact_result = exact_skill_match(
            cv_skills,
            job_skills,
        )
        
        semantic_result = semantic_skill_match(  
            cv_skills,
            job_skills,
        )
        
        score_result = calculate_match_score(
            matched=exact_result["matched"],
            job_skills=job_skills,
            semantic_matches=semantic_result,
        ) 
        
        results.append(
            {
                "job_id": job["job_id"],
                "title": job["title"],
                "matched": exact_result["matched"],
                "missing": exact_result["missing"],
                "semantic_matches": score_result["semantic_matches"],
                "exact_score": score_result["exact_score"],
                "semantic_score": score_result["semantic_score"],
                "overall_score": score_result["overall_score"],
            }           
        )
        
    return rank_jobs(results)